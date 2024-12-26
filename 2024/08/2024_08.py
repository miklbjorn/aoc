from collections import defaultdict

run_on_test = False
input_file = "test_input" if run_on_test else "input"

generators = defaultdict(list)
with open(input_file) as f:
    s = f.read()
with open(input_file) as f:
    for y, l in enumerate(f.readlines()):
        for x, f in enumerate(l.strip()):
            if f != '.':
                generators[f].append((x, y))
Y, X = y+1, x+1

grid = []
for l in s.split('\n'):
    grid.append(list(l))
assert all([len(l1) == len(l2) for l1, l2 in zip(grid[:-1], grid[1:])])
X, Y = len(grid[0]), len(grid)

def _in_bounds(x, y):
    return 0 <= x and x < X and 0 <= y and y < Y

# problem 1
nodes = set()

def get_nodes(generators):
    nodes = set()
    N = len(generators)
    if N == 1:
        return nodes
    for i in range(N-1):
        for j in range(i+1, N):
            g1, g2 = generators[i], generators[j]
            dx, dy = g1[0]-g2[0], g1[1]-g2[1]
            n1 = (g1[0] + dx, g1[1]+dy)
            n2 = (g2[0] - dx, g2[1] - dy)
            if _in_bounds(n1[0], n1[1]):
                nodes.add(n1)
            if _in_bounds(n2[0], n2[1]):
                nodes.add(n2)
    return nodes

for f in generators:
    nodes.update(get_nodes(generators[f]))

print(len(nodes))



def get_nodes_part_2(generators):
    nodes = set()
    N = len(generators)
    if N == 1:
        return nodes
    for i in range(N-1):
        for j in range(i+1, N):
            g1, g2 = generators[i], generators[j]
            dx, dy = g1[0]-g2[0], g1[1]-g2[1]

            x, y = g1
            while True:
                nodes.add((x, y))
                x, y = x + dx, y + dy
                if not _in_bounds(x, y):
                    break

            x, y = g2
            while True:
                nodes.add((x, y))
                x, y = x - dx, y - dy
                if not _in_bounds(x, y):
                    break
    return nodes

nodes = set()
for f in generators:
    nodes.update(get_nodes_part_2(generators[f]))
print(len(nodes))