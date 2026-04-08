"""
Gym Ads Data - Comprehensive Analysis Script
Extracts precise metrics from all CSV files for the analysis report.
"""
import csv
import os
from collections import defaultdict

RAW = "/Users/nguyennghia/Documents/GitHub/gym-ads-data/raw_data"

# ============================================================
# 1. ADS DATA ANALYSIS
# ============================================================
def parse_ads_file(filepath, month_label):
    """Parse a single ads CSV and return list of row dicts."""
    rows = []
    with open(filepath, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for r in reader:
            r["_month"] = month_label
            rows.append(r)
    return rows

ads_files = [
    ("Data-Ads-T1.2026.csv", "T1/2026"),
    ("Data-Ads-T2.2026.csv", "T2/2026"),
    ("Data-Ads-T3.2026.csv", "T3/2026"),
]

all_ads = []
for fname, label in ads_files:
    path = os.path.join(RAW, fname)
    if os.path.exists(path) and os.path.getsize(path) > 600:
        all_ads.extend(parse_ads_file(path, label))

# --- Per-campaign, per-month summary ---
camp_month = defaultdict(lambda: {
    "spend": 0, "impressions": 0, "reach": 0, "results": 0,
    "clicks": 0, "msg_contacts": 0, "new_msg": 0, "msg_started": 0,
    "budget": 0, "indicator": "", "status": ""
})

# --- Per age-gender summary (lead campaigns only) ---
age_gender = defaultdict(lambda: {"spend": 0, "results": 0, "impressions": 0, "reach": 0, "clicks": 0})

# --- Per-month totals ---
month_totals = defaultdict(lambda: {"spend": 0, "impressions": 0, "reach": 0, "results_lead": 0, "results_engagement": 0, "results_msg": 0, "clicks": 0})

for r in all_ads:
    camp = r.get("Campaign name", "").strip()
    month = r["_month"]
    key = (camp, month)
    indicator = r.get("Result indicator", "")

    spend = float(r.get("Amount spent (VND)", 0) or 0)
    impressions = int(float(r.get("Impressions", 0) or 0))
    reach = int(float(r.get("Reach", 0) or 0))
    results = int(float(r.get("Results", 0) or 0))
    clicks = int(float(r.get("Clicks (all)", 0) or 0))
    msg_contacts = int(float(r.get("Total messaging contacts", 0) or 0))
    new_msg = int(float(r.get("New messaging contacts", 0) or 0))
    msg_started = int(float(r.get("Messaging conversations started", 0) or 0))
    budget = float(r.get("Ad set budget", 0) or 0)
    status = r.get("Campaign delivery", "")
    age = r.get("Age", "")
    gender = r.get("Gender", "")

    cm = camp_month[key]
    cm["spend"] += spend
    cm["impressions"] += impressions
    cm["reach"] += reach
    cm["results"] += results
    cm["clicks"] += clicks
    cm["msg_contacts"] += msg_contacts
    cm["new_msg"] += new_msg
    cm["msg_started"] += msg_started
    cm["budget"] = budget
    cm["indicator"] = indicator
    cm["status"] = status

    mt = month_totals[month]
    mt["spend"] += spend
    mt["impressions"] += impressions
    mt["reach"] += reach
    mt["clicks"] += clicks
    if "lead" in indicator:
        mt["results_lead"] += results
    elif "engagement" in indicator:
        mt["results_engagement"] += results
    elif "messaging" in indicator:
        mt["results_msg"] += results

    # Age-gender for lead campaigns
    if "lead" in indicator:
        ag_key = (month, age, gender)
        ag = age_gender[ag_key]
        ag["spend"] += spend
        ag["results"] += results
        ag["impressions"] += impressions
        ag["reach"] += reach
        ag["clicks"] += clicks

print("=" * 80)
print("ADS PERFORMANCE BY CAMPAIGN & MONTH")
print("=" * 80)

for month_label in ["T1/2026", "T2/2026", "T3/2026"]:
    print(f"\n--- {month_label} ---")
    print(f"{'Campaign':<16} {'Status':<10} {'Budget/d':>10} {'Spend':>12} {'Impr':>10} {'Reach':>10} {'Results':>8} {'CPR':>10} {'Clicks':>8} {'CTR':>6} {'MsgCont':>8} {'Type'}")

    camps = [(k, v) for k, v in camp_month.items() if k[1] == month_label]
    camps.sort(key=lambda x: x[1]["spend"], reverse=True)

    total_spend = 0
    total_results = 0
    total_impressions = 0
    total_reach = 0
    total_clicks = 0
    total_msg = 0

    for (camp, _), v in camps:
        cpr = v["spend"] / v["results"] if v["results"] > 0 else 0
        ctr = (v["clicks"] / v["impressions"] * 100) if v["impressions"] > 0 else 0
        indicator_short = "LEAD" if "lead" in v["indicator"] else ("ENGAGE" if "engagement" in v["indicator"] else ("MSG" if "messaging" in v["indicator"] else "?"))

        print(f"{camp:<16} {v['status']:<10} {v['budget']:>10,.0f} {v['spend']:>12,.0f} {v['impressions']:>10,} {v['reach']:>10,} {v['results']:>8,} {cpr:>10,.0f} {v['clicks']:>8,} {ctr:>5.2f}% {v['msg_contacts']:>8,} {indicator_short}")

        total_spend += v["spend"]
        total_results += v["results"]
        total_impressions += v["impressions"]
        total_reach += v["reach"]
        total_clicks += v["clicks"]
        total_msg += v["msg_contacts"]

    print(f"{'TOTAL':<16} {'':10} {'':>10} {total_spend:>12,.0f} {total_impressions:>10,} {total_reach:>10,} {total_results:>8,} {'':>10} {total_clicks:>8,} {'':>6} {total_msg:>8,}")

print("\n" + "=" * 80)
print("MONTHLY TOTALS")
print("=" * 80)
for m in ["T1/2026", "T2/2026", "T3/2026"]:
    mt = month_totals[m]
    cpl = mt["spend"] / mt["results_lead"] if mt["results_lead"] > 0 else 0
    print(f"{m}: Spend={mt['spend']:,.0f} | Leads={mt['results_lead']} | CPL={cpl:,.0f} | Engagements={mt['results_engagement']:,} | MsgResults={mt['results_msg']} | Clicks={mt['clicks']:,} | Impr={mt['impressions']:,}")

print("\n" + "=" * 80)
print("AGE-GENDER BREAKDOWN (Lead campaigns only)")
print("=" * 80)
for month_label in ["T1/2026", "T2/2026", "T3/2026"]:
    print(f"\n--- {month_label} ---")
    print(f"{'Age':<8} {'Gender':<10} {'Spend':>12} {'Results':>8} {'CPL':>10} {'Impr':>10} {'Clicks':>8}")

    age_order = ["18-24", "25-34", "35-44", "45-54", "55-64", "65+"]
    gender_order = ["female", "male", "unknown"]

    # Aggregate across campaigns for this month
    agg = defaultdict(lambda: {"spend": 0, "results": 0, "impressions": 0, "clicks": 0})
    for (m, age, gender), v in age_gender.items():
        if m == month_label:
            agg[(age, gender)]["spend"] += v["spend"]
            agg[(age, gender)]["results"] += v["results"]
            agg[(age, gender)]["impressions"] += v["impressions"]
            agg[(age, gender)]["clicks"] += v["clicks"]

    for age in age_order:
        for gender in gender_order:
            k = (age, gender)
            if k in agg and agg[k]["spend"] > 0:
                v = agg[k]
                cpl = v["spend"] / v["results"] if v["results"] > 0 else float('inf')
                cpl_str = f"{cpl:>10,.0f}" if v["results"] > 0 else "   NO LEAD"
                print(f"{age:<8} {gender:<10} {v['spend']:>12,.0f} {v['results']:>8} {cpl_str} {v['impressions']:>10,} {v['clicks']:>8,}")

# Age totals
print("\n--- AGE TOTALS (all months, lead campaigns) ---")
age_total = defaultdict(lambda: {"spend": 0, "results": 0})
for (m, age, gender), v in age_gender.items():
    if gender != "unknown":
        age_total[age]["spend"] += v["spend"]
        age_total[age]["results"] += v["results"]

for age in ["18-24", "25-34", "35-44", "45-54", "55-64", "65+"]:
    v = age_total[age]
    cpl = v["spend"] / v["results"] if v["results"] > 0 else float('inf')
    cpl_str = f"{cpl:,.0f}" if v["results"] > 0 else "NO LEAD"
    print(f"  {age}: Spend={v['spend']:,.0f} | Leads={v['results']} | CPL={cpl_str}")

# Gender totals
print("\n--- GENDER TOTALS (all months, lead campaigns) ---")
gender_total = defaultdict(lambda: {"spend": 0, "results": 0})
for (m, age, gender), v in age_gender.items():
    gender_total[gender]["spend"] += v["spend"]
    gender_total[gender]["results"] += v["results"]

for g in ["female", "male", "unknown"]:
    v = gender_total[g]
    cpl = v["spend"] / v["results"] if v["results"] > 0 else float('inf')
    cpl_str = f"{cpl:,.0f}" if v["results"] > 0 else "NO LEAD"
    print(f"  {g}: Spend={v['spend']:,.0f} | Leads={v['results']} | CPL={cpl_str}")


# ============================================================
# 2. LEAD ULTRA (CRM) ANALYSIS
# ============================================================
print("\n\n" + "=" * 80)
print("LEAD ULTRA (CRM) ANALYSIS")
print("=" * 80)

lead_files = [
    ("Lead Ultra  - T11.2025.csv", "T11/2025"),
    ("Lead Ultra  - T12.2025.csv", "T12/2025"),
    ("Lead Ultra  - T1.2026.csv", "T1/2026"),
    ("Lead Ultra - T2.2026.csv", "T2/2026"),
]

for fname, label in lead_files:
    path = os.path.join(RAW, fname)
    if not os.path.exists(path):
        continue

    leads = []
    with open(path, encoding="utf-8") as f:
        content = f.read()

    # Parse manually due to multiline headers
    lines = content.split("\n")

    status_count = defaultdict(int)
    source_count = defaultdict(int)
    sale_count = defaultdict(int)
    sale_done = defaultdict(int)
    source_done = defaultdict(int)
    source_status = defaultdict(lambda: defaultdict(int))
    total = 0

    for line in lines[4:]:  # Skip header rows
        parts = line.split(",")
        if len(parts) < 7:
            continue
        try:
            stt = int(parts[0].strip())
        except (ValueError, IndexError):
            continue

        total += 1
        nguon = parts[4].strip() if len(parts) > 4 else ""
        sale = parts[5].strip() if len(parts) > 5 else ""
        tinh_trang = parts[6].strip() if len(parts) > 6 else ""

        status_count[tinh_trang] += 1
        source_count[nguon] += 1
        sale_count[sale] += 1
        source_status[nguon][tinh_trang] += 1

        if "Done" in tinh_trang or "done" in tinh_trang:
            sale_done[sale] += 1
            source_done[nguon] += 1

    print(f"\n--- {label} ({total} leads) ---")

    print(f"\n  STATUS:")
    for s, c in sorted(status_count.items(), key=lambda x: -x[1]):
        pct = c / total * 100 if total > 0 else 0
        print(f"    {s}: {c} ({pct:.1f}%)")

    print(f"\n  SOURCE:")
    for s, c in sorted(source_count.items(), key=lambda x: -x[1]):
        done = source_done.get(s, 0)
        rate = done / c * 100 if c > 0 else 0
        print(f"    {s}: {c} leads | {done} done | {rate:.1f}% close rate")

    print(f"\n  SALE PERFORMANCE:")
    for s, c in sorted(sale_count.items(), key=lambda x: -x[1]):
        done = sale_done.get(s, 0)
        rate = done / c * 100 if c > 0 else 0
        print(f"    {s}: {c} leads | {done} done | {rate:.1f}% close rate")

    print(f"\n  SOURCE x STATUS:")
    for src in sorted(source_status.keys()):
        statuses = source_status[src]
        parts_str = ", ".join(f"{st}:{ct}" for st, ct in sorted(statuses.items(), key=lambda x: -x[1]))
        print(f"    {src}: {parts_str}")

# ============================================================
# 3. CAMPAIGN TYPE ANALYSIS
# ============================================================
print("\n\n" + "=" * 80)
print("CAMPAIGN TYPE SPEND COMPARISON")
print("=" * 80)

for month_label in ["T1/2026", "T2/2026", "T3/2026"]:
    lead_spend = 0
    engage_spend = 0
    msg_spend = 0
    lead_results = 0
    engage_results = 0

    for (camp, m), v in camp_month.items():
        if m != month_label:
            continue
        if "lead" in v["indicator"]:
            lead_spend += v["spend"]
            lead_results += v["results"]
        elif "engagement" in v["indicator"]:
            engage_spend += v["spend"]
            engage_results += v["results"]
        elif "messaging" in v["indicator"]:
            msg_spend += v["spend"]

    total = lead_spend + engage_spend + msg_spend
    print(f"\n{month_label}:")
    print(f"  Lead Gen:    {lead_spend:>12,.0f} VND ({lead_spend/total*100:.1f}%) | {lead_results} leads | CPL={lead_spend/lead_results:,.0f}" if lead_results > 0 else f"  Lead Gen:    {lead_spend:>12,.0f} VND | 0 leads")
    print(f"  Engagement:  {engage_spend:>12,.0f} VND ({engage_spend/total*100:.1f}%) | {engage_results:,} engagements")
    if msg_spend > 0:
        print(f"  Messaging:   {msg_spend:>12,.0f} VND ({msg_spend/total*100:.1f}%)")
    print(f"  TOTAL:       {total:>12,.0f} VND")

print("\n\nDone.")
