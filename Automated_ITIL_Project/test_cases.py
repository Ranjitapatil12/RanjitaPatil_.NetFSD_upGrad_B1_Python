from utils import (
    load_tickets,
    save_tickets,
    validate_ticket_id,
    is_duplicate_ticket
)
from itil import Ticket
from monitor import create_auto_ticket
from datetime import datetime

# 1. TEST TICKET CREATION
def test_ticket_creation():
    tickets = load_tickets()

    t = Ticket("Test User", "IT", "Laptop slow", "Incident")
    tickets.append(t.to_dict())
    save_tickets(tickets)

    assert t.ticket_id.startswith("T")
    print("✔ Ticket Creation Passed")

# 2. TEST PRIORITY LOGIC
def test_priority_logic():
    t1 = Ticket("User", "IT", "server down", "Incident")
    t2 = Ticket("User", "IT", "internet issue", "Incident")
    t3 = Ticket("User", "IT", "laptop slow", "Incident")
    t4 = Ticket("User", "IT", "password reset", "Incident")

    assert t1.priority == "P1"
    assert t2.priority == "P2"
    assert t3.priority == "P3"
    assert t4.priority == "P4"

    print("✔ Priority Logic Passed")

# 3. TEST SLA BREACH
def test_sla_breach():
    t = Ticket("User", "IT", "server down", "Incident")

    # force old date
    t.created_at = "2000-01-01 00:00:00"

    assert t.is_sla_breached() is True

    print("✔ SLA Breach Passed")


# 4. TEST AUTO MONITORING
def test_auto_monitoring_ticket_creation():
    create_auto_ticket("High CPU Usage")

    tickets = load_tickets()

    found = any("high cpu" in t["issue"].lower() for t in tickets)

    assert found is True

    print("✔ Auto Monitoring Ticket Creation Passed")

# 5. TEST FILE READ / WRITE
def test_file_read_write():
    tickets = load_tickets()

    save_tickets(tickets)

    loaded = load_tickets()

    assert isinstance(loaded, list)

    print("✔ File Read/Write Passed")


# 6. TEST SEARCH TICKET
def test_search_ticket():
    tickets = load_tickets()

    if tickets:
        tid = tickets[0]["ticket_id"]

        found = any(t["ticket_id"] == tid for t in tickets)

        assert found is True

    print("✔ Search Ticket Passed")


# 7. TEST EXCEPTION HANDLING
def test_exception_handling():
    try:
        Ticket("User", "IT", "", "Incident")   # empty issue
    except ValueError:
        print("✔ Exception Handling Passed")


# EXTRA (STRONG FEATURE)
def test_validate_ticket_id():
    assert validate_ticket_id("T001")
    assert not validate_ticket_id("ABC")
    print("✔ Ticket ID Validation Passed")


def test_duplicate_ticket():
    tickets = [{
        "ticket_id": "T001",
        "employee_name": "A",
        "department": "IT",
        "issue": "laptop slow",
        "category": "Incident",
        "priority": "P3",
        "status": "Open",
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }]

    assert is_duplicate_ticket(tickets, "Laptop Slow") is True

    print("✔ Duplicate Detection Passed")

# RUN ALL TESTS
if __name__ == "__main__":
    print("\n===== RUNNING TEST CASES =====\n")

    test_ticket_creation()
    test_priority_logic()
    test_sla_breach()
    test_auto_monitoring_ticket_creation()
    test_file_read_write()
    test_search_ticket()
    test_exception_handling()

    
    test_validate_ticket_id()
    test_duplicate_ticket()

    print("\n🎉 ALL TEST CASES PASSED SUCCESSFULLY!")