from datetime import datetime, timedelta

# CUSTOM EXCEPTION
class InvalidTicketException(Exception):
    pass

# BASE TICKET CLASS
class Ticket:
    ticket_counter = 1

    def __init__(self, employee_name, department, issue, category):

        if not issue.strip():
            raise InvalidTicketException("Issue description cannot be empty")

        #  PRIVATE + PUBLIC ACCESS
        self.__ticket_id = f"T{Ticket.ticket_counter:04}"
        self.ticket_id = self.__ticket_id   # 🔥 FIX (IMPORTANT)

        Ticket.ticket_counter += 1

        self.employee_name = employee_name
        self.department = department
        self.issue = issue
        self.category = category

        self.priority = self.assign_priority(issue)
        self.status = "Open"
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.closed_at = None

        self.ticket_type = "General"

    # GETTER (ENCAPSULATION)
    def get_ticket_id(self):
        return self.__ticket_id

    # PRIORITY LOGIC

    def assign_priority(self, issue):
        issue = issue.lower()

        if "server" in issue:
            return "P1"
        elif "internet" in issue:
            return "P2"
        elif "laptop" in issue or "slow" in issue:
            return "P3"
        elif "password" in issue:
            return "P4"
        else:
            return "P3"

    # SLA TIME
    def get_sla_time(self):
        sla_map = {
            "P1": timedelta(hours=1),
            "P2": timedelta(hours=4),
            "P3": timedelta(hours=8),
            "P4": timedelta(hours=24)
        }
        return sla_map[self.priority]

    # SLA CHECK
    def is_sla_breached(self):
        created = datetime.strptime(self.created_at, "%Y-%m-%d %H:%M:%S")
        return datetime.now() > created + self.get_sla_time()

    # TO DICT
    def to_dict(self):
        return {
            "ticket_id": self.ticket_id,   
            "employee_name": self.employee_name,
            "department": self.department,
            "issue": self.issue,
            "category": self.category,
            "priority": self.priority,
            "status": self.status,
            "created_at": self.created_at,
            "closed_at": self.closed_at,
            "ticket_type": self.ticket_type
        }

    # STATIC METHOD
    @staticmethod
    def validate_category(category):
        return category in ["Incident", "Service Request"]


# INCIDENT
class IncidentTicket(Ticket):
    def __init__(self, employee_name, department, issue):
        super().__init__(employee_name, department, issue, "Incident")
        self.ticket_type = "Incident"


# SERVICE REQUEST

class ServiceRequest(Ticket):
    def __init__(self, employee_name, department, issue):
        super().__init__(employee_name, department, issue, "Service Request")
        self.ticket_type = "Service Request"


# PROBLEM RECORD
class ProblemRecord:
    def __init__(self, issue):
        self.problem_id = f"P{int(datetime.now().timestamp())}"
        self.issue = issue
        self.count = 5
        self.status = "Investigating"
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return self.__dict__


# CHANGE REQUEST
class ChangeRequest:
    def __init__(self, description):
        self.change_id = f"C{int(datetime.now().timestamp())}"
        self.description = description
        self.status = "Requested"
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return self.__dict__


# MONITOR
class Monitor:
    def check_threshold(self, cpu, ram, disk):
        alerts = []

        if cpu > 90:
            alerts.append("High CPU Usage")
        if ram > 95:
            alerts.append("High RAM Usage")
        if disk < 10:
            alerts.append("Low Disk Space")

        return alerts


# REPORT GENERATOR
class ReportGenerator:
    def __init__(self, tickets):
        self.tickets = tickets

    def total_tickets(self):
        return len(self.tickets)

    def open_tickets(self):
        return len([t for t in self.tickets if t["status"] == "Open"])

    def closed_tickets(self):
        return len([t for t in self.tickets if t["status"] == "Closed"])

    def high_priority_tickets(self):
        return len([t for t in self.tickets if t["priority"] == "P1"])

    def most_common_issue(self):
        issues = [t["issue"] for t in self.tickets]
        return max(set(issues), key=issues.count) if issues else None

    def department_with_most_tickets(self):
        depts = [t["department"] for t in self.tickets]
        return max(set(depts), key=depts.count) if depts else None

    def avg_resolution_time(self):
        times = []

        for t in self.tickets:
            if t.get("closed_at"):
                start = datetime.strptime(t["created_at"], "%Y-%m-%d %H:%M:%S")
                end = datetime.strptime(t["closed_at"], "%Y-%m-%d %H:%M:%S")
                times.append((end - start).total_seconds() / 3600)

        return round(sum(times)/len(times), 2) if times else 0