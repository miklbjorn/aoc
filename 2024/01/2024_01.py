from collections import defaultdict

run_on_test = False
input_file = "test_input" if run_on_test else "input"

with open(input_file) as f:
    l1 = []
    l2 = []
    for z in f.readlines():
        x, y = z.split(' ', 1)
        l1.append(int(x.strip()))
        l2.append(int(y.strip()))

# problem 1
total = 0
for x, y in zip(sorted(l1), sorted(l2)):
    total += abs(x-y)
print(total)

# problem 2
counts_1 = defaultdict(int)
counts_2 = defaultdict(int)
for x in l1:
    counts_1[x] += 1
for y in l2:
    counts_2[y] += 1
total = 0
for k in l1:
    total += k*counts_2[k]
print(total)