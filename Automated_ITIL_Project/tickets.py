import json
import os
from datetime import datetime
from itil import IncidentTicket, ServiceRequest, Ticket
from logger import log
from utils import detect_problem   

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TICKET_FILE = os.path.join(BASE_DIR, "data", "tickets.json")


# LOAD DATA
def load_data(file_path):
    try:
        if not os.path.exists(file_path):
            return []

        with open(file_path, "r") as f:
            data = json.load(f)
            return data if isinstance(data, list) else []

    except json.JSONDecodeError:
        log("Invalid JSON format", "ERROR")
        return []

    except Exception as e:
        log(f"Load error: {str(e)}", "ERROR")
        return []


# SAVE DATA
def save_data(file_path, data):
    try:
        with open(file_path, "w") as f:
            json.dump(data, f, indent=4)

        print("✅ Data saved successfully")

    except Exception as e:
        log(f"Save error: {str(e)}", "ERROR")
        print("❌ Save failed:", e)


# GENERATE ID
def get_next_ticket_id(tickets):
    if not tickets:
        return "T0001"

    last_id = max(tickets, key=lambda x: int(x["ticket_id"][1:]))["ticket_id"]
    num = int(last_id[1:])
    return f"T{num+1:04}"


# CREATE TICKET
def create_ticket():
    tickets = load_data(TICKET_FILE)

    try:
        name = input("Enter employee name: ").strip().title()
        dept = input("Enter department: ").strip().upper()
        issue = input("Enter issue: ").strip()

        if not name or not dept or not issue:
            raise ValueError("Fields cannot be empty")

        category_input = input("Enter category (Incident/Service Request): ").strip().lower()

        if category_input == "incident":
            category = "Incident"
        elif category_input in ["service request", "service"]:
            category = "Service Request"
        else:
            print("⚠️ Invalid category. Defaulting to Incident")
            category = "Incident"

        # Duplicate warning
        if any(t["issue"].lower() == issue.lower() for t in tickets):
            print("⚠️ Similar issue detected (used for problem tracking)")
            log("Duplicate issue detected", "WARNING")

        # Create object
        if category == "Incident":
            ticket_obj = IncidentTicket(name, dept, issue)
        else:
            ticket_obj = ServiceRequest(name, dept, issue)

        ticket_obj.ticket_id = get_next_ticket_id(tickets)

        ticket_dict = ticket_obj.to_dict()
        tickets.append(ticket_dict)

        save_data(TICKET_FILE, tickets)

        # Reload after saving
        tickets = load_data(TICKET_FILE)

        detect_problem(tickets)

        log(f"Ticket Created - {ticket_obj.ticket_id}", "INFO")
        print(f"✅ Ticket Created: {ticket_obj.ticket_id}")

    except ValueError as e:
        log(str(e), "ERROR")
        print("Error:", e)

    except Exception as e:
        log(str(e), "CRITICAL")
        print("Unexpected Error:", e)


# VIEW
def view_tickets():
    tickets = load_data(TICKET_FILE)

    if not tickets:
        print("No tickets found.")
        return

    tickets = sorted(tickets, key=lambda x: x["priority"])

    for t in tickets:
        temp = Ticket(
            t["employee_name"],
            t["department"],
            t["issue"],
            t["category"]
        )
        temp.created_at = t["created_at"]
        temp.priority = t["priority"]

        if temp.is_sla_breached():
            print("⚠ SLA BREACHED:", t["ticket_id"])

        print(t)


# SEARCH
def search_ticket():
    tickets = load_data(TICKET_FILE)
    tid = input("Enter Ticket ID: ").strip().upper()

    for t in tickets:
        if t["ticket_id"].upper() == tid:
            print(t)
            return

    print("❌ Not found")
    log("Search failed", "WARNING")


# UPDATE
def update_ticket():
    tickets = load_data(TICKET_FILE)
    tid = input("Enter Ticket ID: ").strip().upper()

    for t in tickets:
        if t["ticket_id"].upper() == tid:
            status = input("Enter status (Open/In Progress/Closed): ").title()

            if status not in ["Open", "In Progress", "Closed"]:
                print("❌ Invalid status")
                log("Invalid status update", "ERROR")
                return

            t["status"] = status

            if status == "Closed":
                t["closed_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                log(f"Ticket closed: {tid}", "INFO")

            save_data(TICKET_FILE, tickets)

            print("✅ Updated")
            log(f"Ticket updated: {tid}", "INFO")
            return

    print("❌ Not found")
    log("Update failed", "WARNING")


# DELETE
def delete_ticket():
    tickets = load_data(TICKET_FILE)
    tid = input("Enter Ticket ID: ").strip().upper()

    new = [t for t in tickets if t["ticket_id"].upper() != tid]

    if len(new) == len(tickets):
        print("❌ Not found")
        log("Delete failed", "WARNING")
    else:
        save_data(TICKET_FILE, new)
        print("✅ Deleted")
        log(f"Ticket deleted: {tid}", "WARNING")