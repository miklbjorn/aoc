from collections import Counter
from queue import PriorityQueue

import utils as u

run_on_test = False
input_file = "input"

if run_on_test:
    s="""###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############"""
else:
    with open(input_file) as f:
        s=f.read()

# parse grid
grid = []
for l in s.strip().split('\n'):
    grid.append(list(l.strip()))
assert all([len(l1) == len(l2) for l1, l2 in zip(grid[:-1], grid[1:])])
X, Y = len(grid[0]), len(grid)

for y, l in enumerate(grid):
    for x, v in enumerate(l):
        if v == 'E':
            pos = x, y
            break

min_distances_to_start = dict()
x, y = pos
def shortest_path_to_end(start_pos, target='S'):

    to_check = PriorityQueue()
    to_check.put((0, start_pos))

    while not to_check.empty():
        d, (x, y) = to_check.get()

        if (x, y) in min_distances_to_start:
            continue
        min_distances_to_start[(x, y)] = d

        if grid[y][x] == target:
            break

        for (dx, dy) in u.Adj.Ps:
            if grid[y+dy][x+dx] == "#":
                continue
            score = d + 1
            to_check.put((score, (x+dx, y+dy)))

            #print((score, (x+dx, y+dy), (dx, dy)))
    return d

d = shortest_path_to_end((x, y))

cnt = 0
c = Counter()
for x, y in min_distances_to_start:
    d0 = min_distances_to_start[(x, y)]
    for dx, dy in u.Adj.Ps:
        xn, yn = x + dx, y + dy
        x2n, y2n = xn + dx, yn + dy
        if  x2n not in range(X) or y2n not in range(Y):
            continue
        if not (grid[yn][xn] == '#' and grid[y2n][x2n] != '#'):
            continue
        delta = d0 - min_distances_to_start.get((x+2*dx, y+2*dy) , d0) -2
        if delta > 0:
            c.update([delta])
        if delta > 99:
            cnt += 1

u.print_copy(cnt)

c = Counter()
cnt = 0
Ex, Ey = pos
for (x, y) in min_distances_to_start:
    d0 =  min_distances_to_start[(x, y)]
    for dx in range(-20, 21):
        max_y = 20 - abs(dx)
        for dy in range(-(max_y), max_y+1):
            d1 = min_distances_to_start.get((x+dx, y+dy), d0)
            delta = d0 - d1 - abs(dx) - abs(dy)
            if delta > 99:
                c.update([delta])
                cnt += 1


u.print_copy(cnt)

# for x in sorted([(k, c[k]) for k in c]):
#     print(x[1], x[0])