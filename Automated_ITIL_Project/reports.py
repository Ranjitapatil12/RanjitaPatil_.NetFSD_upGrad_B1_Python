from collections import Counter
from datetime import datetime
from functools import reduce

# DAILY REPORT
def generate_daily_report(tickets):
    total = len(tickets)

    # FILTER (Open + In Progress)
    open_tickets = list(filter(
        lambda t: t["status"].strip().lower() in ["open", "in progress"],
        tickets
    ))

    # FILTER (Closed)
    closed_tickets = list(filter(
        lambda t: t["status"].strip().lower() == "closed",
        tickets
    ))

    # FILTER (High Priority P1)
    high_priority = list(filter(
        lambda t: t["priority"] == "P1",
        tickets
    ))

    sla_breached = 0

    for t in tickets:
        if t["status"].strip().lower() == "closed":
            continue

        created_time = datetime.strptime(
            t["created_at"], "%Y-%m-%d %H:%M:%S"
        )

        sla_map = {
            "P1": 1,
            "P2": 4,
            "P3": 8,
            "P4": 24
        }

        hours = (datetime.now() - created_time).total_seconds() / 3600

        if hours > sla_map[t["priority"]]:
            sla_breached += 1

    print("\n📊 DAILY REPORT")
    print(f"Total Tickets: {total}")
    print(f"Open Tickets: {len(open_tickets)}")
    print(f"Closed Tickets: {len(closed_tickets)}")
    print(f"High Priority (P1): {len(high_priority)}")
    print(f"SLA Breached: {sla_breached}")


# MONTHLY REPORT
def generate_monthly_report(tickets):
    if not tickets:
        print("\n📈 MONTHLY REPORT")
        print("No data available")
        return

    #  MAP (extract fields)
    issues = list(map(lambda t: t["issue"].lower(), tickets))
    departments = list(map(lambda t: t["department"], tickets))

    #  Counter (analysis)
    most_common_issue = Counter(issues).most_common(1)
    top_department = Counter(departments).most_common(1)

    print("\n📈 MONTHLY REPORT")

    if most_common_issue:
        print(f"Most Common Issue: {most_common_issue[0][0]}")

    if top_department:
        print(f"Top Department: {top_department[0][0]}")

    # FILTER (closed tickets only)
    closed_tickets = list(filter(
        lambda t: t["status"].strip().lower() == "closed" and "closed_at" in t,
        tickets
    ))

    # MAP (resolution time)
    def get_resolution_time(t):
        try:
            created = datetime.strptime(
                t["created_at"], "%Y-%m-%d %H:%M:%S"
            )
            closed = datetime.strptime(
                t["closed_at"], "%Y-%m-%d %H:%M:%S"
            )
            return (closed - created).total_seconds()
        except:
            return 0

    resolution_times = list(map(get_resolution_time, closed_tickets))

    # REDUCE (total resolution time)
    total_time = reduce(lambda x, y: x + y, resolution_times, 0)

    if len(resolution_times) > 0:
        avg_hours = total_time / len(resolution_times) / 3600
        print(f"Average Resolution Time: {round(avg_hours, 2)} hours")
    else:
        print("Average Resolution Time: Not enough data")

    #  EXTRA: Total tickets using REDUCE
    total_tickets = reduce(lambda x, _: x + 1, tickets, 0)
    print(f"Total Tickets (via reduce): {total_tickets}")

    # REPEATED PROBLEMS (FINAL FIX)

    problem_tickets = list(filter(
        lambda t: t["category"] == "Problem",
        tickets
    ))
    print(f"Repeated Problems: {len(problem_tickets)}")