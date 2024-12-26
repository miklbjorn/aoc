import utils as u

run_on_test = False
input_file = "test_input" if run_on_test else "input"

if run_on_test:
    s="""AAAA
BBCD
BBCC
EEEC"""
else:
    with open(input_file) as f:
        s=f.read()

# parse grid
grid = []
for l in s.strip().split('\n'):
    grid.append(list(l.strip()))
assert all([len(l1) == len(l2) for l1, l2 in zip(grid[:-1], grid[1:])])
X, Y = len(grid[0]), len(grid)

seen = set()
to_explore = [(0, 0)]

sum, sum2 = 0, 0
while to_explore:
    x, y = to_explore.pop()
    if (x, y) in seen: continue

    seen.add((x, y))
    to_explore_region = [(x, y)]
    _region = set()
    _region_perimeter = set()

    while to_explore_region:
        x, y = to_explore_region.pop()
        print(f"     IN region: ({x},{y}) = {grid[y][x]}")
        seen.add((x, y))
        _region.add((x, y))
        for dx, dy in u.Adj.Ps:
            xn, yn = x + dx, y + dy
            if xn not in range(X) or yn not in range(Y):
                _region_perimeter.add((x, xn, y, yn))
                continue
            if grid[y][x] == grid[yn][xn]:
                if (xn, yn) not in seen and (xn, yn) not in to_explore_region:
                    to_explore_region.append((x+dx, y+dy))
            else:
                _region_perimeter.add((x, xn, y, yn))
                if (xn, yn) not in seen:
                    to_explore.append((x+dx, y+dy))
    sum += len(_region) * len(_region_perimeter)

    sides = 0
    while _region_perimeter:
        x, xn, y, yn = _region_perimeter.pop()
        if x == xn:
            # horizontal
            i, j = 1, 1
            while (x+i, xn+i, y, yn) in _region_perimeter:
                _region_perimeter.remove((x+i, xn+i, y, yn))
                i += 1
            while (x - j, xn - j, y, yn) in _region_perimeter:
                _region_perimeter.remove((x - j, xn -j, y, yn))
                j += 1
        elif y == yn:
            # vertical
            i, j = 1, 1
            while (x, xn, y + i, yn + i) in _region_perimeter:
                _region_perimeter.remove((x, xn, y + i, yn + i))
                i += 1
            while (x, xn, y - j, yn - j) in _region_perimeter:
                _region_perimeter.remove((x, xn, y - j, yn - j))
                j += 1
        else:
            raise ValueError
        sides += 1
    print(f'SIDES: {sides}')
    sum2 += len(_region) * sides


u.print_copy(sum)
u.print_copy(sum2)

