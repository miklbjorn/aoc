from collections import Counter, deque

import utils as u

run_on_test = False
input_file = "input"

if run_on_test:
    s="""1
2
3
2024"""
else:
    with open(input_file) as f:
        s=f.read()

# parse lines
lines = []
for l in s.strip().split('\n'):
    lines.append(int(l))

N = 2000

def mix(i, j):
    return i ^ j

def prune(i):
    return i % (1 << 24)

def update(i):
    j = i << 6
    i = prune(mix(i, j))
    j = i >> 5
    i = prune(mix(i, j))
    j = i << 11
    return prune(mix(i, j))

sum = 0
for i in lines:
    for n in range(N):
        i = update(i)
    sum += i

u.print_copy(sum)

# problem 2
N=2000
bananas = Counter()
for i in lines:
    changes = deque()
    prices = {}
    for n in range(N):
        i, old_p = update(i), i % 10
        delta = (new_p := i % 10) - old_p
        changes.append(delta)
        if len(changes) > 4:
            changes.popleft()
        if len(changes) == 4:
            index = tuple(d for d in changes)
            if not index in prices:
                prices[index] = new_p
    bananas.update(prices)

max, max_i = 0, None
for k in bananas:
    if bananas[k] > max:
        max, max_i = bananas[k], k

u.print_copy(max)


# 1733 was wrong
# 1771 was too high