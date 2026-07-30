#!/usr/bin/env python3
"""Convert real contrib.json data into contributions.json format for render_heatmap_svg.py"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))

# Load the real data from contrib.json
real = json.load(open(os.path.join(HERE, 'contrib.json')))
contribs = real['contributions']

# Convert to the format expected by render_heatmap_svg.py
days = [{'date': c['date'], 'count': c['count']} for c in contribs]
days.sort(key=lambda d: d['date'])

total = sum(d['count'] for d in days)
active_days = sum(1 for d in days if d['count'] > 0)
best = max(days, key=lambda d: d['count'])

# Current streak
cur_streak = 0
i = len(days) - 1
while i >= 0 and days[i]['count'] > 0:
    cur_streak += 1
    i -= 1
cur_start = days[i+1]['date'] if cur_streak > 0 else None
cur_end = days[-1]['date'] if cur_streak > 0 else None

# Longest streak
longest = run = 0
longest_start = longest_end = None
run_start = None
for i, d in enumerate(days):
    if d['count'] > 0:
        if run == 0:
            run_start = i
        run += 1
        if run > longest:
            longest = run
            longest_start = days[run_start]['date']
            longest_end = days[i]['date']
    else:
        run = 0

# Monthly
monthly = {}
for d in days:
    key = d['date'][:7]
    monthly[key] = monthly.get(key, 0) + d['count']
monthly_list = [{'month': k, 'total': v} for k, v in sorted(monthly.items())]

result = {
    'username': 'mridul2507',
    'generated_at': days[-1]['date'] + 'T00:00:00Z',
    'range': {'start': days[0]['date'], 'end': days[-1]['date']},
    'total_contributions': total,
    'active_days': active_days,
    'avg_per_active_day': round(total / active_days, 1) if active_days else 0,
    'current_streak': {'length': cur_streak, 'start': cur_start, 'end': cur_end},
    'longest_streak': {'length': longest, 'start': longest_start, 'end': longest_end},
    'best_day': {'date': best['date'], 'count': best['count']},
    'monthly': monthly_list,
    'days': days
}

out_path = os.path.join(HERE, '..', 'data', 'contributions.json')
with open(out_path, 'w') as f:
    json.dump(result, f, indent=2)

print(f'Written to {out_path}')
print(f'Total: {total} contributions')
print(f'Active days: {active_days}')
print(f'Date range: {days[0]["date"]} to {days[-1]["date"]}')
print(f'Current streak: {cur_streak} days')
print(f'Longest streak: {longest} days')
print(f'Best day: {best["date"]} with {best["count"]} contributions')
print(f'Number of days: {len(days)}')
