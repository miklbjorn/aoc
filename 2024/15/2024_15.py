import utils as u

run_on_test = False
input_file = "input"

if run_on_test:
    inp="""##########
#......O.#
#......O.#
#.OOO..O.#
#.OO@O.O.#
##########

<>><^"""
else:
    with open(input_file) as f:
        inp=f.read()

s, ms = inp.split('\n\n')

# parse lines
ms= ''.join(ms.split('\n'))

# parse grid
grid = [[z for z in x.strip()] for x in s.split('\n')]
for y, ss  in enumerate(grid):
    for x, v in enumerate(ss):
        if v == '@': pos = (x, y)
assert all([len(l1) == len(l2) for l1, l2 in zip(grid[:-1], grid[1:])])
X, Y = len(grid[0]), len(grid)

moves = {
    '^': (0, -1),
    '<': (-1, 0),
    '>': (1, 0),
    'v': (0, 1),
}

x, y = pos
for j, m in enumerate(ms):
    dx, dy = moves[m]
    grid[y][x] = '.'
    if grid[y+dy][x+dx] == '.':
        x, y = x + dx, y + dy
    elif grid[y+dy][x+dx] == '#':
        pass
    elif grid[y+dy][x+dx] == 'O':
        i = 1
        while grid[y+i*dy][x+i*dx] == 'O':
            i += 1
        if grid[y+i*dy][x+i*dx] == '#':
            pass
        elif grid[y+i*dy][x+i*dx] == '.':
            grid[y + i * dy][x + i * dx] = 'O'
            x, y = x + dx, y + dy
    grid[y][x] = '@'

score = 0
for y, ss  in enumerate(grid):
    for x, v in enumerate(ss):
        if v == 'O': score += (x + 100*y)

u.print_copy(score)

s2 = s.strip().replace('.', '..').replace('#', '##').replace('O', '[]').replace('@', '@.')

# parse grid
grid = [[z for z in x.strip()] for x in s2.split('\n')]
for y, ss  in enumerate(grid):
    for x, v in enumerate(ss):
        if v == '@': pos = (x, y)
assert all([len(l1) == len(l2) for l1, l2 in zip(grid[:-1], grid[1:])])
X, Y = len(grid[0]), len(grid)

def _move(boxes, dx, dy):
    for box, (x, y) in boxes:
        dx_box = 1 if box == '[' else -1
        grid[y][x] = '.'
        grid[y][x+dx_box] = '.'
    for box, (x, y) in boxes:
        grid[y + dy][x + dx] = box
        if box == '[':
            grid[y+dy][x+dx+1] = ']'
        else:
            grid[y + dy][x + dx - 1] = '['

for s in grid:
    print(''.join(s))
print('....')
x, y = pos
for j, m in enumerate(ms):
    dx, dy = moves[m]
    grid[y][x] = '.'
    boxes_to_move = set()
    boxes_to_check = set()
    if grid[y+dy][x+dx] == '.':
        x, y = x + dx, y + dy
    elif grid[y+dy][x+dx] == '#':
        pass
    elif grid[y+dy][x+dx] in '[]':
        if dx == 0:
            boxes_to_check.add((grid[y+dy][x+dx], (x+dx, y+dy)))
            while len(boxes_to_check):
                box, (bx, by) = boxes_to_check.pop()
                boxes_to_move.add((box, (bx, by)))
                dx_box = 1 if box == '[' else -1
                for (cx, cy) in [(bx, by+dy), (bx+dx_box, by+dy)]:
                    if grid[cy][cx] == '#':
                        boxes_to_check = set()
                        boxes_to_move = set()
                        break
                    elif grid[cy][cx] == '.':
                        pass
                    elif grid[cy][cx] in '[]':
                        boxes_to_check.add((grid[cy][cx], (cx, cy)))
            if len(boxes_to_move):
                x, y = x + dx, y + dy
            # movnig up or down
        else:
            target = '[' if dx == 1 else ']'
            i = 1
            while grid[y + i * dy][x + i * dx] == target:
                boxes_to_move.add((target, (x+i*dx, y+i*dy)))
                i += 2
            if grid[y + i * dy][x + i * dx] == "#":
                boxes_to_move = set()
                pass
            elif grid[y + i * dy][x + i * dx] == '.':
                x, y = x + dx, y + dy

    _move(boxes_to_move, dx, dy)
    grid[y][x] = '@'

for s in grid:
    print(''.join(s))

score = 0
for y, ss  in enumerate(grid):
    for x, v in enumerate(ss):
        if v == '[': score += (x + 100*y)
u.print_copy(score)
