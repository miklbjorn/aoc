import re

import utils as u

run_on_test = False
input_file = "input"

if run_on_test:
    s="""r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb"""
else:
    with open(input_file) as f:
        s=f.read()

s1, s2 = s.split('\n\n')

match = f"({'|'.join([cs.strip() for cs in s1.split(',')])})*"

colors = [cs.strip() for cs in s1.split(',')]

hits = 0

checks = s2.strip().split('\n')

# colors = ['r', 'rw', 'rb', 'uw']
# checks = ['rbuw']

for j, x in enumerate(checks):

    fails = set()

    def _check(i):
        if i in fails:
            return False
        if i == len(x):
            return True
        #print(j, i)
        found = False
        for c in colors:
            if i+len(c) > len(x):
                pass
            elif c == x[i:i+len(c)]:
                if _check(i+len(c)):
                    found = True
                    break
        if not found:
            fails.add(i)
        return found

    if _check(0):
        print(j, x)
        hits = hits + 1
    else:
        print('XXX', j, x)
print('----')
u.print_copy(hits)
print('----')

hits = 0
for j, x in enumerate(checks):

    counts = {}
    n_ways = 0

    def _check(i):
        n_check = 0
        if i in counts:
            return counts[i]
        if i == len(x):
            counts[i] = 1
            return counts[i]
        for c in colors:
            if i + len(c) > len(x):
                pass
            elif c == x[i:i + len(c)]:
                n_check = n_check + _check(i + len(c))

        counts[i] = n_check
        return counts[i]

    n = _check(0)
    print(j, x, n)
    hits = hits + n
u.print_copy(hits)

