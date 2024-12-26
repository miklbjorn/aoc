import utils as u

run_on_test = False
input_file = "input"

if run_on_test:
    s="""p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3"""
else:
    with open(input_file) as f:
        s=f.read()

# parse lines
lines = []
X, Y = 101, 103
n = 100
q1, q2, q3, q4 = 0,0,0,0

import numpy as np
a = np.zeros((Y, X))

ps = []
for l in s.strip().split('\n'):
    x, y, vx, vy = u.nums(l)
    ps.append([x, y, vx, vy])

    x = (x + vx*n) % X
    y = (y + vy*n) % Y
    if y < Y//2 and x > X//2:
        q1 += 1
    elif y < Y // 2 and x < X // 2:
        q2 += 1
    elif y > Y//2 and x > X//2:
        q4 += 1
    elif y > Y // 2 and x < X // 2:
        q3 += 1
    a[y, x] += 1

u.print_copy(q1*q2*q3*q4)

i = 0
xv, yv = [], []
while i < max(X, Y):
    xds, yds = [], []
    for j, (x, y, vx, vy) in enumerate(ps):
        xn = (x + i*vx) % X
        yn = (y + i*vy) % Y
        yds.append(yn)
        xds.append(xn)
    xv.append(np.sqrt(np.var(xds)))
    yv.append(np.sqrt(np.var(yds)))
    i+=1

# ADMISSION OF GUILT
# I started looking for one large connected component. Then Hugo woke up
# logging into reddit -> immediately saw variance plots and chinese remainder thm spoilers ...

# hacky way to check variance is small for exactly one move in x or y respectively
# for i, yd in enumerate(yv):
#     print(f'{i:3d}: {xd/np.min(yv)}')

# these are the number of moves minimisig variance in x and y dirs, respectively
bx = np.argmin(xv)
by = np.argmin(yv)

# now we need to find k such that
# k % Y = by
# k % X = bx
# by def k = bx + t * X
for t in range(Y):
    if (bx + t * X) % Y == by:
        break
u.print_copy(bx+t*X)

# prettu plt
seen = set()
for l in s.strip().split('\n'):
    x, y, vx, vy = u.nums(l)
    seen.add(((x+bx*vx) % X, (y+by*vy)%Y))

print('\n'.join([''.join(['A' if (x, y) in seen else ' ' for x in range(X)]) for y in range(Y)]))