from copy import deepcopy

import utils as u

run_on_test = False
input_file = "test_input" if run_on_test else "input"

if run_on_test:
    s="""89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""
else:
    with open(input_file) as f:
        s=f.read()

# parse grid
grid = []
for l in s.strip().split('\n'):
    grid.append([-2 if x =='.' else int(x) for x in list(l)])
assert all([len(l1) == len(l2) for l1, l2 in zip(grid[:-1], grid[1:])])
X, Y = len(grid[0]), len(grid)

scores = {}


def _score(x, y):
    if y not in range(Y) or x not in range(X):
        scores[(x,y)] = 0
    elif (x, y) in scores:
        return scores[(x,y)]
    elif grid[y][x] == 9:
        scores[(x, y)] = set([(x, y)])
    else:
        neighbours = [_score(x+dx, y+dy)
                             for dx, dy in [u.Adj.N, u.Adj.E, u.Adj.S, u.Adj.W]
                             if (y+dy in range(Y)
                                 and x+dx in range(X)
                                 and grid[y+dy][x+dx] - grid[y][x] == 1)
                      ]
        score = set()
        for n in neighbours:
            score = score.union(n)
        scores[(x, y)] = score
    return scores[(x, y)]

score = 0
for x in range(X):
    for y in range(Y):
        if grid[y][x]:
            continue
        score = score+len(_score(x, y))

def _print_scores(scores):
    _g = deepcopy(grid)
    for x in range(X):
        for y in range(Y):
            if (x, y) in scores:
                _g[y][x] = str(len(scores[(x, y)])).rjust(2, ' ')
            else:
                _g[y][x] = ' .'
    for l in _g:
        print(l)

u.print_copy(score)


scores = {}
def _score(x, y):
    if y not in range(Y) or x not in range(X):
        scores[(x,y)] = 0
    elif (x, y) in scores:
        return scores[(x,y)]
    elif grid[y][x] == 9:
        scores[(x, y)] = 1
    else:
        neighbours = [_score(x+dx, y+dy)
                             for dx, dy in [u.Adj.N, u.Adj.E, u.Adj.S, u.Adj.W]
                             if (y+dy in range(Y)
                                 and x+dx in range(X)
                                 and grid[y+dy][x+dx] - grid[y][x] == 1)
                      ]
        scores[(x, y)] = sum(neighbours) if neighbours else 0
    return scores[(x, y)]

score = 0
for x in range(X):
    for y in range(Y):
        if grid[y][x]:
            continue
        score = score+_score(x, y)

u.print_copy(score)