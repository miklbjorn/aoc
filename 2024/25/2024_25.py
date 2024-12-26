import utils as u

run_on_test = False
input_file = "input"

if run_on_test:
    s="""#####
.####
.####
.####
.#.#.
.#...
.....

#####
##.##
.#.##
...##
...#.
...#.
.....

.....
#....
#....
#...#
#.#.#
#.###
#####

.....
.....
#.#..
###..
###.#
###.#
#####

.....
.....
.....
#....
#.#..
#.#.#
#####"""
else:
    with open(input_file) as f:
        s=f.read()

ss = s.strip().split('\n\n')
locks = []
keys = []
for x in ss:
    counts = tuple(sum(c == '#' for c in r)-1 for r in zip(*x.split('\n')))
    if x.startswith('#'):
        locks.append(counts)
    else:
        keys.append(counts)

print(len(locks), len(keys))

sum = 0
for l in locks:
    for k in keys:
        fit = True
        for i in range(5):
            if k[i] + l[i] > 5:
                fit = False
                break
        if fit:
            sum += 1

u.print_copy(sum)