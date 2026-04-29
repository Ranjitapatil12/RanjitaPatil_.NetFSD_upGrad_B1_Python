import psutil
from itil import IncidentTicket
from tickets import load_data, save_data, TICKET_FILE
from logger import log


# NETWORK USAGE FUNCTION
def get_network_usage():
    net = psutil.net_io_counters()
    return net.bytes_sent + net.bytes_recv


# SYSTEM MONITORING
def monitor_system():
    try:
        cpu = psutil.cpu_percent(interval=1)
        ram = psutil.virtual_memory().percent
        disk_usage = psutil.disk_usage('/').percent
        disk_free = 100 - disk_usage   
        network = get_network_usage()

        print(f"\nCPU: {cpu}% | RAM: {ram}% | Disk Used: {disk_usage}%")
        print(f"Network Usage: {network} bytes")

        alert_triggered = False

        # THRESHOLDS
        if cpu > 90:
            create_auto_ticket("High CPU Usage")
            alert_triggered = True

        if ram > 95:
            create_auto_ticket("High Memory Usage")
            alert_triggered = True

        # CORRECT LOGIC (IMPORTANT)
        if disk_free < 10:
            create_auto_ticket("Low Disk Space")
            alert_triggered = True

        if network > 100000000:  # ~100MB
            create_auto_ticket("High Network Usage")
            alert_triggered = True

        if not alert_triggered:
            log("Monitoring check completed: no alerts", "INFO")

    except Exception as e:
        log(f"Monitoring Error: {str(e)}", "ERROR")
        print("Error:", e)


# AUTO TICKET CREATION
def create_auto_ticket(issue):
    try:
        tickets = load_data(TICKET_FILE)

        # DUPLICATE PREVENTION
        for t in tickets:
            if (
                t["issue"].strip().lower() == issue.lower()
                and t["status"] != "Closed"
                and t.get("category") == "Incident"
            ):
                log(f"Duplicate auto ticket prevented: {issue}", "WARNING")
                return

        # CREATE NEW TICKET
        ticket_obj = IncidentTicket("System", "IT", issue)
        ticket_obj.priority = "P1"   # force critical

        ticket_dict = ticket_obj.to_dict()
        tickets.append(ticket_dict)

        save_data(TICKET_FILE, tickets)

        # LOGGING (MANDATORY)
        log(f"Auto Ticket Created - {ticket_dict['ticket_id']} ({issue})", "CRITICAL")

        print(f"🚨 Auto Ticket Created: {ticket_dict['ticket_id']} ({issue})")

    except Exception as e:
        log(f"Auto Ticket Error: {str(e)}", "ERROR")
        print("Error creating auto ticket:", e)