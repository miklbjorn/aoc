from queue import PriorityQueue

import utils as u

run_on_test = False
input_file = "input"

if run_on_test:
    s="""5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0"""
    X, Y = 6, 6
    n = 12
else:
    X, Y = 70, 70
    n = 1024
    with open(input_file) as f:
        s=f.read()

# parse lines
lines = []
drops = {}
drop_list = []
for i, l in enumerate(s.strip().split('\n')):
    x, y = u.nums(l)
    drops[(x, y)] = i
    drop_list.append((x, y))


to_check = PriorityQueue()
min_distances_to_start = {}

to_check.put((0, (0, 0)))

def shortest_path_to_end(n):
    to_check = PriorityQueue()
    min_distances_to_start = {}
    to_check.put((0, (0, 0)))
    found=False
    while not to_check.empty():
        d, (x, y) = to_check.get()

        if (x, y) in min_distances_to_start:
            continue
        min_distances_to_start[(x, y)] = d

        if (x, y) == (X, Y):
            found = True
            break

        for (dx, dy) in u.Adj.Ps:
            if (x+dx, y+dy) in drops and drops[(x+dx, y+dy)] < n:
                continue
            if not (x+dx in range(X+1) and y+dy in range(Y+1)):
                continue
            score = d + 1
            to_check.put((score, (x+dx, y+dy)))
    if not found:
        d = -1
    return d

u.print_copy(shortest_path_to_end(n))

# a bit of barbarian brute force ...
for i in range(n+1, len(drops)-1):
    if shortest_path_to_end(i) < 0:
        print(i)
        print(drop_list[i-1])
        break