import re

import pyperclip

class Adj:
    N = (0, 1)
    E = (1, 0)
    S = (0, -1)
    W = (-1, 0)

    Ps = [N, E, S, W]

def nums(s):
    return [int(x) for x in re.findall('(-{0,1}\\d+)', s)]


def get_rim(X, Y):
    """Yield all (x, y) points along rim of grid with lengths X and Y"""
    x, y = 0, 0
    yield x, y
    while x+1 < X:
        yield (x:= x+1), y
    while y+1 < Y:
        yield x, (y := y+1)
    while x:
        yield (x:= x-1), y
    while y-1:
        yield x, (y := y-1)

def print_copy(s):
    """Print value and copyt o clipboard."""
    print(s)
    pyperclip.copy(s)

