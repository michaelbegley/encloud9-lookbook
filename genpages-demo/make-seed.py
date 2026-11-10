#!/usr/bin/env python3
"""Write the Generative Pages demo seed CSVs with every date set relative to the demo day.

Usage:  python3 make-seed.py YYYY-MM-DD [--out DIR] [--hour 12]

All companies, people, emails (example.com) and phone numbers (555) are fictional.
Every date is an offset in days from the demo day, so the pages show the same picture on any day.
After writing, it prints the badge each account (page 2) and each open opportunity (page 1) gets
under the rules in PROMPTS.md (relationship health and deal health), assuming the demo runs at --hour.
(Copied 10 Nov 2026 from the project file claude/genpages-demo/make-seed.py, Agent 18, 4 Nov 2026.)
"""
import argparse
import csv
import datetime as dt
import os
import re

# ---------------------------------------------------------------------------------------------
# Fictional data, with offsets in days from the demo day (negative = before the demo).
# ---------------------------------------------------------------------------------------------
ACCOUNTS = [
    # name, industry (standard option label, confirm), city, state, employees, annual revenue
    ("Bluegill Freight Co", "Transportation", "Omaha", "NE", 42, 8200000),
    ("Cedar Point Dental Group", "Doctor's Offices and Clinics", "Lincoln", "NE", 65, 12500000),
    ("Harbor Lane Bakery", "Food and Tobacco Processing", "Des Moines", "IA", 18, 2100000),
    ("Ironwood Fabrication", "Durable Manufacturing", "Kansas City", "MO", 120, 31000000),
    ("Juniper Ridge Outfitters", "Service Retail", "Sioux Falls", "SD", 33, 5400000),
    ("Kestrel Analytics", "Consulting", "Denver", "CO", 27, 6100000),
    ("Lakeshore Home Health", "Doctor's Offices and Clinics", "Madison", "WI", 210, 44000000),
    ("Maple Hollow Logistics", "Transportation", "Topeka", "KS", 88, 19500000),
    ("Prairie Wind Energy", "Utility Creation and Distribution", "Wichita", "KS", 150, 52000000),
    ("Quarry Street Legal", "Legal Services", "Minneapolis", "MN", 24, 7300000),
]
FIRST = ["Avery", "Blake", "Casey", "Devon", "Emerson", "Finley", "Gray", "Harper", "Indy", "Jordan",
         "Kai", "Logan", "Morgan", "Noel", "Oakley", "Parker", "Quinn", "Reese", "Sawyer", "Taylor"]
LAST = ["Abernathy", "Bellweather", "Castellano", "Dunmore", "Everly", "Fairbanks", "Greenvale", "Holloway",
        "Iverson", "Jessup", "Kowalczyk", "Larkspur", "Merriweather", "Northcott", "Ostrander", "Pemberton",
        "Quillan", "Ravenscroft", "Stanfield", "Thackeray"]
TITLES = ["Operations Director", "CFO", "IT Manager", "Office Manager", "VP Sales", "Controller", "Owner", "Project Lead"]

# Write-in products and unit prices (fictional catalogue).
PRICE = {
    "Discovery workshop": 4000,
    "Configuration sprint": 8000,
    "Data migration": 10000,
    "Integration build": 12000,
    "Training day": 2000,
    "Power BI report pack": 5000,
}

# Opportunities: topic, account index, probability, close offset, state, product lines [(product, qty)].
# Open opportunities: Est. Revenue is the exact sum of their product lines, so the products and the tile agree
# whether Dynamics calculates revenue from products or not.
OPPORTUNITIES = [
    ("Fleet telematics rollout", 0, 60, 45, "open", [("Configuration sprint", 5), ("Training day", 4)]),
    ("Patient portal integration", 1, 40, 75, "open", [("Integration build", 5), ("Training day", 6)]),
    ("Online ordering pilot", 2, 70, 20, "open", [("Configuration sprint", 1), ("Discovery workshop", 2)]),
    ("Shop floor scheduling", 3, 50, 110, "open", [("Configuration sprint", 12), ("Integration build", 3)]),
    ("Loyalty program CRM", 4, 30, 150, "open", [("Configuration sprint", 2), ("Data migration", 1)]),
    ("Analytics workspace setup", 5, 80, 12, "open", [("Power BI report pack", 6), ("Configuration sprint", 1)]),
    ("Care coordination app", 6, 20, 170, "open", [("Configuration sprint", 15), ("Data migration", 4)]),
    ("Dispatch board modernization", 7, 55, 95, "open", [("Configuration sprint", 6), ("Training day", 8)]),
    ("Field service mobile", 8, 45, 130, "open", [("Configuration sprint", 10), ("Training day", 9)]),
    ("Matter intake automation", 9, 65, -10, "open", [("Configuration sprint", 2), ("Training day", 3)]),
    # closed after import by hand (no products): topic, account, probability, close offset, state, revenue
    ("Driver onboarding forms", 0, 100, -40, "won", 12000),
    ("Hygiene recall reminders", 1, 100, -25, "won", 18000),
    ("Supplier portal", 3, 100, -60, "won", 54000),
    ("Seasonal staffing tracker", 4, 0, -35, "lost", 9000),
    ("Energy usage dashboard", 8, 0, -15, "lost", 41000),
]

# Quotes: name, opportunity index, discount percent. Lines copy the opportunity's product lines.
QUOTES = [
    ("Q-DEMO fleet telematics phase 1", 0, 5),
    ("Q-DEMO patient portal", 1, 12),
    ("Q-DEMO online ordering", 2, 0),
    ("Q-DEMO shop floor scheduling", 3, 18),
    ("Q-DEMO analytics workspace", 5, 8),
    ("Q-DEMO dispatch board", 7, 25),
    ("Q-DEMO field service mobile", 8, 15),
    ("Q-DEMO matter intake", 9, 3),
]

# Cases (open): title, account index, priority. Lakeshore gets two High cases (At risk by the case rule).
CASES = [
    ("Login fails after password reset", 1, "High"),
    ("Report shows wrong totals", 3, "Normal"),
    ("Duplicate contacts created", 6, "High"),
    ("Appointment reminders not sending", 6, "High"),
    ("Request new user setup", 9, "Low"),
]

# Phone calls regarding ACCOUNTS (page 2 reads activities regarding the account):
# account index, offset, completed. Harbor Lane has none (At risk: no completed activity).
CALLS = [
    (0, -9, True),    # Bluegill        -> Strong
    (1, -20, True),   # Cedar Point     -> Steady (1 High case, 20 days)
    (3, -5, True),    # Ironwood        -> Strong (5 days, Normal case only)
    (4, -30, True),   # Juniper Ridge   -> Steady
    (5, -3, True),    # Kestrel         -> Strong
    (6, -10, True),   # Lakeshore       -> At risk (2 High cases)
    (7, -50, True),   # Maple Hollow    -> At risk (over 45 days)
    (8, -16, True),   # Prairie Wind    -> Steady
    (9, -7, True),    # Quarry Street   -> Strong (Low case only)
    (4, 3, False),    # Juniper Ridge, open call due in 3 days
]

# Tasks regarding OPPORTUNITIES (page 1 reads activities regarding the opportunity):
# opportunity index, offset, completed.
TASKS = [
    (0, -8, True),    # Fleet telematics      -> green
    (1, -20, True),   # Patient portal        -> amber
    (2, 4, False),    # Online ordering       -> red (no completed activity)
    (3, -5, True),    # Shop floor scheduling -> green
    (3, -2, False),   # Shop floor scheduling: OPEN and 2 days overdue, shows red in the timeline
    (4, -12, True),   # Loyalty program       -> green
    (5, -2, True),    # Analytics workspace   -> green
    (6, -25, True),   # Care coordination     -> amber
    (7, 6, False),    # Dispatch board        -> red (no completed activity)
    (8, -10, True),   # Field service mobile  -> green
]


def domain(name):
    return re.sub(r"[^a-z]", "", name.lower()) + ".example.com"


def contacts():
    out = []
    for i in range(20):
        acc = ACCOUNTS[i // 2][0]
        out.append((FIRST[i], LAST[i], TITLES[i % len(TITLES)], acc))
    return out


def write(path, header, rows):
    with open(path, "w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(header)
        writer.writerows(rows)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("demo_date", help="demo day, YYYY-MM-DD")
    parser.add_argument("--out", default=os.path.dirname(os.path.abspath(__file__)))
    parser.add_argument("--hour", type=int, default=12, help="hour of day the demo runs, for the badge check")
    args = parser.parse_args()
    demo = dt.datetime.strptime(args.demo_date, "%Y-%m-%d")
    day = lambda offset: (demo + dt.timedelta(days=offset)).strftime("%m/%d/%Y")
    stamp = lambda offset: (demo + dt.timedelta(days=offset)).strftime("%m/%d/%Y") + " 08:00 AM"
    out = args.out
    people = contacts()

    write(os.path.join(out, "01-accounts.csv"),
          ["Account Name", "Industry", "Address 1: City", "Address 1: State/Province", "Number of Employees",
           "Annual Revenue", "Website", "Main Phone"],
          [[n, ind, c, s, e, r, "https://www." + domain(n), f"402-555-01{i:02d}"]
           for i, (n, ind, c, s, e, r) in enumerate(ACCOUNTS)])

    write(os.path.join(out, "02-contacts.csv"),
          ["First Name", "Last Name", "Job Title", "Email", "Business Phone", "Company Name"],
          [[f, l, t, f"{f.lower()}.{l.lower()}@{domain(a)}", f"402-555-02{i:02d}", a]
           for i, (f, l, t, a) in enumerate(people)])

    opp_rows, product_rows = [], []
    for topic, ai, prob, off, state, extra in OPPORTUNITIES:
        account = ACCOUNTS[ai][0]
        contact = f"{people[ai * 2][0]} {people[ai * 2][1]}"
        value = sum(PRICE[p] * q for p, q in extra) if state == "open" else extra
        opp_rows.append([topic, account, contact, value, prob, day(off), f"Demo opportunity for {account}."])
        if state == "open":
            for product, qty in extra:
                product_rows.append([topic, product, "Write-in", PRICE[product], qty])
    write(os.path.join(out, "03-opportunities.csv"),
          ["Topic", "Account", "Contact", "Est. Revenue", "Probability", "Est. Close Date", "Description"], opp_rows)
    write(os.path.join(out, "04-opportunity-products.csv"),
          ["Opportunity", "Write-In Product", "Select Product", "Price Per Unit", "Quantity"], product_rows)

    quote_rows, quote_line_rows = [], []
    for name, oi, discount in QUOTES:
        topic, ai, _, _, _, lines = OPPORTUNITIES[oi]
        quote_rows.append([name, ACCOUNTS[ai][0], topic, "<CONFIRM: price list name in the demo environment>", discount, "Pending"])
        for product, qty in lines:
            quote_line_rows.append([name, product, "Write-in", PRICE[product], qty])
    write(os.path.join(out, "05-quotes.csv"),
          ["Name", "Potential Customer", "Opportunity", "Price List", "Quote Discount (%)", "Approval Status"], quote_rows)
    write(os.path.join(out, "06-quote-products.csv"),
          ["Quote", "Write-In Product", "Select Product", "Price Per Unit", "Quantity"], quote_line_rows)

    write(os.path.join(out, "07-cases.csv"),
          ["Case Title", "Customer", "Priority", "Origin", "Description"],
          [[t, ACCOUNTS[ai][0], pr, "Phone", f"Demo case for {ACCOUNTS[ai][0]}."] for t, ai, pr in CASES])

    write(os.path.join(out, "08-tasks.csv"),
          ["Subject", "Regarding", "Due", "Actual End", "Activity Status"],
          [[f"Follow up: {OPPORTUNITIES[oi][0]}", OPPORTUNITIES[oi][0], stamp(off), stamp(off) if done else "",
            "Completed" if done else "Open"] for oi, off, done in TASKS])

    write(os.path.join(out, "09-phone-calls.csv"),
          ["Subject", "Regarding", "Due", "Actual End", "Direction", "Activity Status"],
          [[f"Check-in call with {ACCOUNTS[ai][0]}", ACCOUNTS[ai][0], stamp(off), stamp(off) if done else "", "Outgoing",
            "Completed" if done else "Open"] for ai, off, done in CALLS])

    report(demo.replace(hour=args.hour))


# ---------------------------------------------------------------------------------------------
# Badge check: the page rules, re-written in Python.
# ---------------------------------------------------------------------------------------------
DAY_MS = 24 * 60 * 60 * 1000


def account_badge(ai, now):
    # Account 360 relationship health: days = floor((now - last completed actualend) / DAY);
    # At risk if no completed activity, days > 45, or 2+ open High cases; Strong if days < 14 and 0 High; else Steady.
    done = [(now + dt.timedelta(days=off)).replace(hour=8, minute=0) for a, off, ok in CALLS if a == ai and ok]
    high = sum(1 for _, a, pr in CASES if a == ai and pr == "High")
    if not done:
        return "At risk", "no completed activity", high
    days = int(((now - max(done)).total_seconds() * 1000) // DAY_MS)
    if days > 45 or high >= 2:
        return "At risk", f"{days} days, {high} High", high
    if days < 14 and high == 0:
        return "Strong", f"{days} days, {high} High", high
    return "Steady", f"{days} days, {high} High", high


def opportunity_badge(oi, now):
    # Opportunity command center deal health: red if close date passed; red if no completed
    # activity or none for over 30 days; amber if over 14 days; else green.
    topic, _, _, close_off, _, _ = OPPORTUNITIES[oi]
    close = (now + dt.timedelta(days=close_off)).replace(hour=0, minute=0)
    if close < now:
        return "At risk (red)", "close date has passed"
    done = [(now + dt.timedelta(days=off)).replace(hour=8, minute=0) for o, off, ok in TASKS if o == oi and ok]
    if not done:
        return "At risk (red)", "no completed activity"
    days = int(((now - max(done)).total_seconds() * 1000) // DAY_MS)
    if days > 30:
        return "At risk (red)", f"no activity for {days} days"
    if days > 14:
        return "Watch (amber)", f"last activity {days} days ago"
    return "Healthy (green)", f"last activity {days} days ago"


def report(now):
    print(f"Badge check for {now:%Y-%m-%d %H:%M} (demo time)")
    print("Page 2, Account 360:")
    for ai, account in enumerate(ACCOUNTS):
        badge, why, _ = account_badge(ai, now)
        print(f"  {account[0]:<28} {badge:<8} ({why})")
    print("Page 1, open opportunities:")
    for oi, opp in enumerate(OPPORTUNITIES):
        if opp[4] != "open":
            continue
        badge, why = opportunity_badge(oi, now)
        value = sum(PRICE[p] * q for p, q in opp[5])
        close = (now + dt.timedelta(days=opp[3])).strftime("%Y-%m-%d")
        print(f"  {opp[0]:<30} ${value:>9,}  close {close}  {badge} ({why})")
    overdue = [OPPORTUNITIES[oi][0] for oi, off, ok in TASKS if not ok and off < 0]
    print("Open overdue tasks (red in the timeline):", ", ".join(overdue))
    print("Quotes (lines = opportunity products; total after discount):")
    for name, oi, discount in QUOTES:
        gross = sum(PRICE[p] * q for p, q in OPPORTUNITIES[oi][5])
        print(f"  {name:<34} ${gross:>9,} less {discount:>2}% = ${gross * (100 - discount) / 100:>11,.2f}")


if __name__ == "__main__":
    main()
