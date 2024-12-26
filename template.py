import utils as u

run_on_test = True
input_file = "input"

if run_on_test:
    s=""""""
else:
    with open(input_file) as f:
        s=f.read()

# parse lines
lines = []
for l in s.strip().split('\n'):
    lines.append(l)

# parse grid
grid = []
for l in s.strip().split('\n'):
    grid.append(list(l.strip()))
assert all([len(l1) == len(l2) for l1, l2 in zip(grid[:-1], grid[1:])])
X, Y = len(grid[0]), len(grid)

