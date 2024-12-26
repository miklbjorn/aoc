import utils as u
import numpy as np

run_on_test = False
input_file = "input"

if run_on_test:
    s="""Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279"""
else:
    with open(input_file) as f:
        s=f.read()

ms = s.split("\n\n")

sum, sum2 = 0, 0
for m in ms:
    sm = m.split("\n")
    x1, y1 = u.nums(sm[0])
    x2, y2 = u.nums(sm[1])
    X , Y  = u.nums(sm[2])

    X = X + 10000000000000
    Y = Y + 10000000000000

    A = np.array([[x1, x2], [y1, y2]])
    if x1/y1*y2/x2 == 1.0:
        print("!")
    if np.linalg.det(A) == 0:
        print('Failed: DET!')
        continue
    x, y = np.dot(np.linalg.inv(A), np.array([X, Y]))
    won1 = False
    if x >= -0.5 and y >= -0.5 and abs(x -round(x)) <0.01 and abs(y-round(y)) <= 0.01:
        #print(np.dot(A, np.array([x, y])),np.array([X, Y]))
        sum += round(3 * x +y)
        won1 = True

    else:
        ...
        #print('Failed', x, y)

    # prettier solution, Cramer's rule
    xn = (X * y2 - x2 * Y) / (x1 * y2 - y1 * x2)
    yn = -(X * y1 - x1 * Y) / (x1 * y2 - y1 * x2)
    if xn > 0 and abs(xn-round(xn)) < 0.01 and yn > 0 and abs(yn - round(yn)) < 0.01:
        sum2 += int(3*xn + yn)

u.print_copy(sum)
u.print_copy(sum2)
