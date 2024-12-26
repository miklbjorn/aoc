import re
from collections import defaultdict

run_on_test = False
input_file = "test_input" if run_on_test else "input"


must_be_smaller = defaultdict(list)
must_be_larger = defaultdict(list)
def _add_rule(l):
    small, large = l.strip().split('|')
    must_be_smaller[small].append(large)
    must_be_larger[large].append(small)

reports = []
def _add_report(l):
    reports.append(l.strip().split(','))

with open(input_file) as f:
    lines = f.readlines()
    for i, l in enumerate(lines):
        if not l.strip(): break
        _add_rule(l)

    for l in lines[i+1:]:
        _add_report(l)

# problem 1
safe_reports = []
unsafe_reports = []
def _is_safe(report):
    for i in range(len(report)-1):
        for j in range(i+1, len(report)):
            if report[j] in must_be_larger[report[i]]:
                return False
    return True

for i, r in enumerate(reports):
    safe = _is_safe(r)
    print(i, safe)
    if safe:
        safe_reports.append(r)
    else:
        unsafe_reports.append(r)

sum = 0
for r in safe_reports:
    sum += int(r[int(len(r)/2)])
print(sum)

# problem 2
def _fix_report(report):
    for i in range(len(report)-1):
        for j in range(i+1, len(report)):
            if report[j] in must_be_larger[report[i]]:
                report[j], report[i] = report[i], report[j]
                return _fix_report(report)
    return report

fixed_reports = [_fix_report(r) for r in unsafe_reports]
sum = 0
for r in fixed_reports:
    sum += int(r[int(len(r)/2)])
print(sum)