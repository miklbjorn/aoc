import math
import re
from collections import deque

import utils as u

run_on_test = False
input_file = "input"

if run_on_test:
    s="""[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]"""
else:
    with open(input_file) as f:
        s=f.read()

def add(a, b):
    return f'[{a},{b}]'

NUMS='0123456789'

def explode(a):
    stack = deque()
    ln = []
    to_explode = ''
    for i, c in enumerate(a):
        if c in NUMS:
            if not len(stack) == 5:
                ln = ln + [i] if (ln and i == ln[-1] + 1) else [i]
        else:
            if c == '[':
                stack.append('[')
            elif c == ']':
                stack.pop()
                if to_explode:
                    break

        if len(stack) == 5:
            to_explode += c
    if not to_explode:
        return a

    n1, n2 = u.nums(to_explode)
    e1, e2 = i-len(to_explode), i+1
    nn = []
    while i < len(a):
        if a[i] not in NUMS and nn:
            break
        if a[i] in NUMS:
            nn.append(i)
        i += 1
    n1 = n1 + int(a[ln[0]:ln[-1]+1]) if ln else n1
    n2 = n2 + int(a[nn[0]:nn[-1]+1]) if nn else n2
    if ln and nn:
        return a[:ln[0]] + str(n1) + a[ln[-1]+1:e1] + '0' + a[e2:nn[0]] + str(n2) + a[nn[-1]+1:]
    elif nn:
        return a[:e1] + '0' + a[e2:nn[0]] + str(n2) + a[nn[-1]+1:]
    elif ln:
        return a[:ln[0]] + str(n1) + a[ln[-1]+1:e1] + '0' + a[e2:]
    else:
        a[:e1] + '0' + a[e2:]

def split(a):
    hit = re.search('(\\d{2,})', a)
    if hit is None:
        return a
    x, y = hit.span()[0], hit.span()[1]
    n = int(a[x:y])
    n1, n2 = int(n/2), math.ceil(n/2)
    return a[:x] + f'[{n1},{n2}]' + a[y:]
def reduce(a):
    while True:
        ao = a
        a = explode(a)
        if a != ao:
            continue
        a = split(a)
        if a != ao:
            continue
        return a

def magnitude(a):
    while hit := re.search('\\d{1,},\\d{1,}', a):
        n1, n2 = u.nums(hit.group())
        x, y = hit.span()
        a = a[:x-1] + str(3*n1 + 2*n2) + a[y+1:]
    return int(a)

ns = [x.strip() for x in s.strip().split('\n')]
n = reduce(add(ns[0], ns[1]))
for nn in ns[2:]:
    n = reduce(add(n, nn))

print(n)
print(magnitude(n))

mag = 0
for n1 in ns:
    for n2 in ns:
        this_mag = magnitude(reduce(add(n1, n2)))
        mag = this_mag if this_mag > mag else mag


print(mag)