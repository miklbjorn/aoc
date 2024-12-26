import utils as u

run_on_test = False
input_file = "input"

if run_on_test:
    s="""###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
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

from queue import PriorityQueue

to_check = PriorityQueue()
to_check_end = PriorityQueue()
min_distances_to_start = {}
min_distances_to_end   = {}

for y, r in enumerate(grid):
    for x, v in enumerate(r):
        if v == 'S':
            to_check.put((0, (x, y), u.Adj.E))
        if v == 'E':
            to_check_end.put((0, (x, y), u.Adj.N))
            print(x, y)

def shortest_path_to_end(to_check, min_distances_to_start = None, target='E', target_d = None):
    if min_distances_to_start is None:
        min_distances_to_start = {}
    while not to_check.empty():
        d, (x, y), dir = to_check.get()

        if ((x, y), dir) in min_distances_to_start:
            continue
        min_distances_to_start[((x, y), dir)] = d

        if grid[y][x] == target:
            break

        for (dx, dy) in u.Adj.Ps:
            if grid[y+dy][x+dx] == "#":
                continue
            score = d + 1
            if dir != (dx, dy):
                score += 1000
            to_check.put((score, (x+dx, y+dy), (dx, dy)))

            #print((score, (x+dx, y+dy), (dx, dy)))
    return d

shortest_path = shortest_path_to_end(to_check, min_distances_to_start)
shortest_path_reversed = shortest_path_to_end(to_check_end, min_distances_to_end, target='S')

hits = set()
for (pos, dir) in min_distances_to_start:
    min_dist_to_end = shortest_path
    for rev_dir in u.Adj.Ps:
        if (pos, rev_dir) in min_distances_to_end:
            c_dist = min_distances_to_end[(pos, rev_dir)]
            if not (rev_dir[0]==-dir[0] and rev_dir[1]==-dir[1]):
                c_dist = c_dist + 1000
            min_dist_to_end = min(min_dist_to_end, c_dist)
    dir_start = min_distances_to_start[(pos, dir)]
    if min_dist_to_end+dir_start <= shortest_path:
        hits.add(pos)

u.print_copy(shortest_path)
u.print_copy(len(hits))
#
# to_check_reversed = PriorityQueue()
# for i, p in enumerate(min_distances_to_start):
#     pos, dir = p
#     d = min_distances_to_start[p]
#     to_check_reversed.put((-d, pos, dir))
# #
# n_hits = 0
# hits = set()
# i = 0
# while not to_check_reversed.empty():
#     if (i := i+1 ) % 500 == 0:
#         print(to_check_reversed.qsize())
#     d, pos, dir = to_check_reversed.get()
#     dist_to_start = -d
#     q = PriorityQueue()
#     q.put((0, pos, dir))
#     dist_to_end = shortest_path_to_end(q, target_d=shortest_path-d)
#     #min_distances_to_end[(pos, dir)] = dist_to_end
#     if dist_to_end + dist_to_start <= shortest_path:
#         n_hits += 1
#         hits.add(pos)
#
# u.print_copy(len(hits))
#
print('\n'.join([''.join([v if not (x, y) in hits else 'O' for x, v in enumerate(g)]) for y, g in enumerate(grid)]))