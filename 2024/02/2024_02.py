run_on_test = False
input_file = "test_input" if run_on_test else "input"

with open(input_file) as f:
    reports = []
    for l in f.readlines():
        levels = [int(n) for n in l.split(' ')]
        reports.append(levels)

# problem 1
def is_safe(levels):
    d_1 = levels[1]-levels[0]
    for d_i, d_ip in zip(levels[:-1], levels[1:]):
        delta = d_ip-d_i
        if abs(delta) > 3:
            return False
        if delta * d_1 <= 0:
            return False
    return True

print(sum(is_safe(l) for l in reports))

def is_safe_with_dampener(levels):
    d_1 = levels[1]-levels[0]
    if is_safe(levels[1:]):
        return True
    if is_safe([levels[0]]+levels[2:]):
        return True
    for i, (d_i, d_ip) in enumerate(zip(levels[:-1], levels[1:])):
        delta = d_ip-d_i
        if abs(delta) > 3:
            levels.pop(i+1)
            return is_safe(levels)
        if delta * d_1 <= 0:
            levels.pop(i + 1)
            return is_safe(levels)
    return True

print(sum(is_safe_with_dampener(l) for l in reports))