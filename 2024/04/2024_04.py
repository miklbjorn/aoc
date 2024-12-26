import re

run_on_test = False
input_file = "test_input" if run_on_test else "input"

with open(input_file) as f:
    lines = [l.strip() for l in f.readlines()]

Y, X = len(lines[0]), len(lines)
target = 'XMAS'
n = len(target)
all_lines = []

# problem 1
def diagonal(start_x, start_y, delta_x, delta_y):
    x, y = start_x, start_y
    line = []
    while (x >= 0 and x<X) and (y >=0 and y < Y):
        line.append(lines[y][x])
        x, y = x + delta_x, y + delta_y
    return ''.join(line)

start_y = 0
for start_x in range(0, X):
    for delta_x, delta_y in [(-1, 1), (0, 1), (1, 1)]:
        if len(line := diagonal(start_x, start_y, delta_x, delta_y)) > 3:
            all_lines.append(line)

start_y = Y - 1
for start_x in range(0, X):
    for delta_x, delta_y in [(-1, -1), (0, -1), (1, -1)]:
        if len(line := diagonal(start_x, start_y, delta_x, delta_y)) > 3:
            all_lines.append(line)

start_x = 0
for start_y in range(0, Y):
    for delta_x, delta_y in [(1, -1), (1, 0), (1, 1)]:
        if start_y == 0 and delta_y == 1:
            continue
        if start_y == Y-1 and delta_y == -1:
            continue
        if len(line := diagonal(start_x, start_y, delta_x, delta_y)) > 3:
            all_lines.append(line)

start_x = X - 1
for start_y in range(0, Y):
    for delta_x, delta_y in [(-1, -1), (-1, 0), (-1, 1)]:
        if start_y == 0 and delta_y == 1:
            continue
        if start_y == Y-1 and delta_y == -1:
            continue
        if len(line := diagonal(start_x, start_y, delta_x, delta_y)) > 3:
            all_lines.append(line)


match_pattern = 'XMAS'
matches = sum(len(re.findall(match_pattern, line)) for line in all_lines)

print(matches)

# problem 2
count = 0
for x in range(1, X-1):
    for y in range(1, Y-1):
        if not lines[y][x] == 'A':
            continue
        if not ((lines[y-1][x-1] == 'M' and lines[y+1][x+1] == 'S') or (lines[y-1][x-1] == 'S' and lines[y+1][x+1] == 'M')):
            continue
        if not ((lines[y-1][x+1] == 'M' and lines[y+1][x-1] == 'S') or (lines[y-1][x+1] == 'S' and lines[y+1][x-1] == 'M')):
            continue
        count += 1
print(count)