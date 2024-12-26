run_on_test = False
input_file = "test_input" if run_on_test else "input"

lines = []
with open(input_file) as f:
    lines = [c.strip() for c in f.readlines()]
Y, X = len(lines), len(lines[0])

for y in range(Y):
    for x in range(X):
        if lines[y][x] == '^':
            starting_position = x, y

position = starting_position
starting_direction = (0, -1) # starting up
dx, dy = starting_direction

def _rotate_right(dx, dy):
    dx, dy = -1*dy , 1*dx
    return dx, dy

def _has_obstacle(x, y):
    return lines[y][x] == '#'

def _in_bounds(x, y):
    return 0 <= x and x < X and 0 <= y and y < Y

# problem 1
visited_positions = {position: 1}
x, y = position
while True:
    if not _in_bounds(x + dx, y + dy):
        break
    if _has_obstacle(x+dx, y+dy):
        dx, dy = _rotate_right(dx, dy)
        continue
    else:
        x, y = x + dx, y + dy
        visited_positions[(x, y)] = 1

print(len(visited_positions))

# problem 2
loops_detected = 0
for obs_x, obs_y in visited_positions.keys():
    if (obs_x, obs_y) == starting_position:
        continue

    x, y = starting_position
    dx, dy = starting_direction
    visited_positions_with_delta = {(x, y, dx, dy): 1}
    while True:
        if not _in_bounds(x + dx, y + dy):
            break
        if _has_obstacle(x+dx, y+dy) or (x + dx == obs_x and y + dy == obs_y):
            dx, dy = _rotate_right(dx, dy)
            continue
        else:
            x, y = x + dx, y + dy
            if (x, y, dx, dy) in visited_positions_with_delta:
                loops_detected += 1
                break
            visited_positions_with_delta[(x, y, dx, dy)] = 1

print(loops_detected)