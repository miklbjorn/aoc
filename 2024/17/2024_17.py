import math

import utils as u

run_on_test = False
input_file = "input"

if run_on_test:
    s = """"""
else:
    with open(input_file) as f:
        s = f.read()

s, p = s.split('\n\n')
A, B, C = u.nums(s)
p = u.nums(p)

# length of program is ~ log2(A)/3
# -> there are 1e15 different programs!





cmds = {
    0: 'adv A = A / 2**',
    1: 'bxl B = B ^',
    2: 'bst B = 8mod ',
    3: 'jnz jump to',
    4: 'bxc B = B ^ C',
    5: 'out Print 8mod',
    6: 'bdv B = A / 2**',
    7: 'cdv C = A / 2**',
}

for j in range(8):
    op, lit_opr = p[2*j], p[2*j + 1]
    combo_opr = lit_opr
    match lit_opr:
        case 4:
            combo_opr = 'A'
        case 5:
            combo_opr = 'B'
        case 6:
            combo_opr = 'C'

    print(cmds[op], combo_opr)

def run(A, B, C):
    out = []
    i = 0
    while i < len(p)-1:
        op, lit_opr = p[i], p[i + 1]
        combo_opr = lit_opr
        match lit_opr:
            case 4:
                combo_opr = A
            case 5:
                combo_opr = B
            case 6:
                combo_opr = C

        match op:
            case 0:
                A = int(A/math.pow(2, combo_opr))
            case 1:
                B = B ^ lit_opr
            case 2:
                B = combo_opr % 8
            case 3:
                if A:
                    i = lit_opr
                    continue
            case 4:
                B = B ^ C
            case 5:
                out.append(combo_opr % 8)
            case 6:
                B = int(A / math.pow(2, combo_opr))
            case 7:
                C = int(A / math.pow(2, combo_opr))
        i += 2
    return out
out = run(A, B, C)
print('-')
u.print_copy(','.join([str(x) for x in out]))


new_As = [0]
checks = 0
for n in reversed(p):
    # logic: find As that match each program number one at a time
    # starting with the last number
    # intuition: last number is a function of 3 leftmost bits in A only
    # next-to-last number is a function of 6 leftmost bits only
    # so find 3 bits that give ;
    old_As = new_As.copy()
    new_As = []
    for A in old_As:
        for i in range(8):
            checks = checks + 1
            out = run((A<<3) + i, 0, 0)
            if out[0] == n:
                new_As.append((A << 3) + i)

u.print_copy(min(new_As))

