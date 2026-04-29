from tickets import (
    create_ticket,
    view_tickets,
    search_ticket,
    update_ticket,
    delete_ticket
)
from monitor import monitor_system
from reports import generate_daily_report, generate_monthly_report
from itil import ChangeRequest
from logger import log
from utils import (
    load_tickets,
    check_sla,
    check_escalation,
    detect_problem,
    save_change_request
)

# CHANGE MANAGEMENT
def create_change_request():
    desc = input("Enter change description: ").strip()

    if not desc:
        print("❌ Description cannot be empty")
        log("Empty change request attempted", "ERROR")
        return

    change = ChangeRequest(desc)
    save_change_request(change.to_dict())

    log(f"Change request created: {change.change_id}", "INFO")
    print(f"✅ Change Request Created: {change.change_id}")

# MONITORING MODULE
def run_monitoring():
    monitor_system()

    tickets = load_tickets()

    check_sla(tickets)
    check_escalation(tickets)
    detect_problem(tickets)

# MENU
def menu():
    while True:
        tickets = load_tickets()

        print("\n===== AUTOMATED ITIL SERVICE DESK =====")
        print("1. Create Ticket")
        print("2. View Tickets")
        print("3. Search Ticket")
        print("4. Update Ticket Status")
        print("5. Delete Ticket")
        print("6. Daily Report")
        print("7. Monthly Report")
        print("8. Monitor System")
        print("9. Create Change Request")
        print("10. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            create_ticket()

        elif choice == "2":
            view_tickets()

        elif choice == "3":
            search_ticket()

        elif choice == "4":
            update_ticket()

        elif choice == "5":
            delete_ticket()

        elif choice == "6":
            generate_daily_report(tickets)

        elif choice == "7":
            generate_monthly_report(tickets)

        elif choice == "8":
            run_monitoring()

        elif choice == "9":
            create_change_request()

        elif choice == "10":
            print("👋 Exiting system...")
            break

        else:
            print("❌ Invalid input. Please try again.")
            log("Invalid menu input", "ERROR")

# ENTRY POINT
if __name__ == "__main__":
    menu()