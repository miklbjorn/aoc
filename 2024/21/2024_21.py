from collections import Counter
from functools import cache

import utils as u

run_on_test = False
input_file = "input"

if run_on_test:
    s="""029A
980A
179A
456A
379A"""
else:
    with open(input_file) as f:
        s=f.read()

# parse lines
ns = {
    'A': (2, 3),
    '0': (1, 3),
    '1': (0, 2),
    '2': (1, 2),
    '3': (2, 2),
    '4': (0, 1),
    '5': (1, 1),
    '6': (2, 1),
    '7': (0, 0),
    '8': (1, 0),
    '9': (2, 0),
}
ms = {
    'A': (2, 0),
    '^': (1, 0),
    '<': (0, 1),
    'v': (1, 1),
    '>': (2, 1),
}

codes = [l for l in s.strip().split('\n')]


def parse_nums(code):
    r1 = ''
    pos = ns['A']
    for c in code:
        new_pos = ns[c]
        r1 += get_moves(pos, new_pos, (0, 3))
        pos = new_pos
    return r1


@cache
def get_moves(pos, new_pos, danger):
    dx, dy = new_pos[0] - pos[0], new_pos[1] - pos[1]

    cx = '<' if dx < 0 else '>'
    cy = '^' if dy < 0 else 'v'

    # Trick is to find preferred order of x and y moves for fewest overall moves
    # once the downstream robot moves are taken into account
    # I did it the fast way ... print and count!
    # for x in '<^', '<v', '^<', 'v<', '>^', '>v', '^>', 'v>':
    #     print(x, parse_moves(parse_moves(x + 'A')))
    # print('-')
    # for x in '<<^^', '^^<<', '<^<^', '^<^<':
    #     print(x, parse_moves(parse_moves(x + 'A')))
    if dx < 0:
        if new_pos[0] == danger[0] and pos[1] == danger[1]:
            return abs(dy) * cy + abs(dx) * cx + 'A'
        else:
            return abs(dx) * cx + abs(dy) * cy + 'A'
    else:
        if new_pos[1] == danger[1] and pos[0] == danger[0]:
            return abs(dx) * cx + abs(dy) * cy + 'A'
        else:
            return abs(dy) * cy + abs(dx) * cx + 'A'

@cache
def parse_moves(moves):
    r2 = ''
    pos = ms['A']
    for c in moves:
        new_pos = ms[c]
        r2 += get_moves(pos, new_pos, (0, 0))
        pos = new_pos
    return r2
def parse(code):
    r1 = parse_nums(code)
    r2 = parse_moves(r1)
    r3 = parse_moves(r2)

    return r1, r2, r3

cnt = 0
for c in codes:
    r1, r2, s = parse(c)
    cnt += len(s) * int(c[:-1])
    print(c, len(s), int(c[:-1]))

u.print_copy(cnt)

def parse_move_counts(counts):
    # instead of keeping track of exploding length move strings:
    # count number of substrings split by A - small set of those exist
    # transform each of them, keep track of new counts - repeat
    new_counts = Counter()
    for k in counts:
        moves = parse_moves(k) # parse_moves is cachec
        s = moves.split('A')
        k_counts = Counter(s[:-1])
        new_counts.update(
            {j + 'A': k_counts[j] * counts[k] for j in k_counts}
        )
    return new_counts



counter = Counter()

def bf_long_parse(code):
    # cracks at around 18 robots ...
    r = parse_nums(code)
    for i in range(5):
        r = parse_moves(r)
    return r

cnt = 0
for c in codes:
    r = bf_long_parse(c)
    n = len(r)
    cnt += n * int(c[:-1])
    print(c, n, int(c[:-1]))
u.print_copy(cnt)

def long_parse(code):
    r = parse_nums(code)
    counts = Counter(r.split('A')[:-1])
    counts = {j + 'A': counts[j] for j in counts}
    for i in range(25):
        counts = parse_move_counts(counts)
    return counts

cnt = 0
for c in codes:
    counts = long_parse(c)
    n = sum(len(k)*counts[k] for k in counts)
    cnt += n * int(c[:-1])
    print(c, n, int(c[:-1]))
u.print_copy(cnt)

# for x in 'v<<', '<v<', '<<v':
#     print(x, parse_moves(parse_moves(x + 'A')))