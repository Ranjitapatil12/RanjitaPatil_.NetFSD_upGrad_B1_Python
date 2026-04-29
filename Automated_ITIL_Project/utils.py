import json
import os
import csv
import re
from datetime import datetime
from logger import log

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

TICKET_FILE = os.path.join(BASE_DIR, "data", "tickets.json")
BACKUP_FILE = os.path.join(BASE_DIR, "data", "backup.csv")
PROBLEM_FILE = os.path.join(BASE_DIR, "data", "problems.json")
CHANGE_FILE = os.path.join(BASE_DIR, "data", "changes.json")

# DECORATOR
def log_function(func):
    def wrapper(*args, **kwargs):
        log(f"Running function: {func.__name__}", "INFO")
        return func(*args, **kwargs)
    return wrapper

# SAFE JSON LOAD
def safe_load_json(file_path):
    try:
        if not os.path.exists(file_path):
            return []

        with open(file_path, "r") as file:
            try:
                data = json.load(file)
                return data if isinstance(data, list) else []
            except:
                return []

    except Exception as e:
        log(f"Error loading file: {e}", "ERROR")
        return []


# LOAD TICKETS
def load_tickets():
    return safe_load_json(TICKET_FILE)

# SAVE TICKETS
def save_tickets(tickets):
    try:
        with open(TICKET_FILE, "w") as file:
            json.dump(tickets, file, indent=4)
    except Exception as e:
        log(f"Error saving tickets: {e}", "ERROR")

# SAVE PROBLEM RECORD
def save_problem_record(problem):
    try:
        data = safe_load_json(PROBLEM_FILE)
        data.append(problem)

        with open(PROBLEM_FILE, "w") as f:
            json.dump(data, f, indent=4)

        log("Problem record saved", "INFO")

    except Exception as e:
        log(f"Error saving problem record: {e}", "ERROR")

# SAVE CHANGE REQUEST

def save_change_request(change):
    try:
        data = safe_load_json(CHANGE_FILE)
        data.append(change)

        with open(CHANGE_FILE, "w") as f:
            json.dump(data, f, indent=4)

        log("Change request saved", "INFO")

    except Exception as e:
        log(f"Error saving change request: {e}", "ERROR")


# GENERATOR
def ticket_generator(tickets):
    for t in tickets:
        yield t

# REGEX VALIDATION
def validate_ticket_id(tid):
    return re.fullmatch(r"T\d{3,4}", tid) is not None

# GENERATE TICKET ID (ROBUST)
def generate_ticket_id(tickets):
    if not tickets:
        return "T0001"

    try:
        last_id = max(tickets, key=lambda x: x["ticket_id"])["ticket_id"]
        num = int(last_id[1:])
        return f"T{num+1:04}"
    except:
        return f"T{len(tickets)+1:04}"

# DUPLICATE CHECK
def is_duplicate_ticket(tickets, issue):
    for t in tickets:
        if (
            t["issue"].strip().lower() == issue.strip().lower()
            and t["status"] != "Closed"
        ):
            return True
    return False


# SORT TICKETS
def sort_tickets(tickets):
    return sorted(tickets, key=lambda x: x["created_at"])

# BACKUP CSV
def backup_to_csv(tickets):
    try:
        with open(BACKUP_FILE, "w", newline="") as file:
            writer = csv.writer(file)

            writer.writerow([
                "Ticket ID", "Name", "Department",
                "Issue", "Category", "Priority",
                "Status", "Created At"
            ])

            for t in tickets:
                writer.writerow([
                    t["ticket_id"],
                    t["employee_name"],
                    t["department"],
                    t["issue"],
                    t["category"],
                    t["priority"],
                    t["status"],
                    t["created_at"]
                ])

        log("Backup CSV created", "INFO")

    except Exception as e:
        log(f"Backup error: {e}", "ERROR")


# SLA CHECK
def check_sla(tickets):
    updated = False
    breach_found = False

    for t in tickets:
        if t["status"] == "Closed":
            continue

        created_time = datetime.strptime(t["created_at"], "%Y-%m-%d %H:%M:%S")

        sla_map = {
            "P1": 1,
            "P2": 4,
            "P3": 8,
            "P4": 24
        }

        hours_passed = (datetime.now() - created_time).total_seconds() / 3600

        if hours_passed > sla_map[t["priority"]] and not t.get("sla_breached"):
            print(f"🚨 SLA BREACHED: {t['ticket_id']}")
            log(f"SLA breached: {t['ticket_id']}", "WARNING")
            t["sla_breached"] = True
            updated = True
            breach_found = True

    if not breach_found:
        log("SLA check completed: no breaches", "INFO")

    if updated:
        save_tickets(tickets)

# ESCALATION CHECK
def check_escalation(tickets):
    updated = False

    for t in tickets:
        if t["status"] == "Closed":
            continue

        created_time = datetime.strptime(t["created_at"], "%Y-%m-%d %H:%M:%S")
        minutes_passed = (datetime.now() - created_time).total_seconds() / 60

        if t["priority"] == "P1" and minutes_passed > 30 and not t.get("escalated"):
            print(f"⚠️ ESCALATION ALERT (P1): {t['ticket_id']}")
            log(f"Escalation alert: {t['ticket_id']}", "WARNING")
            t["escalated"] = True
            updated = True

        elif t["priority"] == "P2" and minutes_passed > 120 and not t.get("escalated"):
            print(f"⚠️ ESCALATION ALERT (P2): {t['ticket_id']}")
            log(f"Escalation alert: {t['ticket_id']}", "WARNING")
            t["escalated"] = True
            updated = True

    if updated:
        save_tickets(tickets)

# PROBLEM DETECTION
def detect_problem(tickets):
    issue_count = {}

    for t in tickets:
        issue = t["issue"].strip().lower()
        issue_count[issue] = issue_count.get(issue, 0) + 1

    for issue, count in issue_count.items():

        if count >= 5:

            already_exists = any(
                t["issue"].strip().lower() == issue and t["category"] == "Problem"
                for t in tickets
            )

            if already_exists:
                continue

            new_ticket = {
                "ticket_id": generate_ticket_id(tickets),
                "employee_name": "System",
                "department": "IT",
                "issue": issue,
                "category": "Problem",
                "priority": "P1",
                "status": "Open",
                "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }

            tickets.append(new_ticket)

            save_tickets(tickets)
            backup_to_csv(tickets)
            save_problem_record(new_ticket)

            log(f"Problem record created: {new_ticket['ticket_id']}", "CRITICAL")

            print(f"🔥 PROBLEM RECORD CREATED: {new_ticket['ticket_id']} ({issue})")