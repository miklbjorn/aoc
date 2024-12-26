from collections import defaultdict

import utils as u

run_on_test = False
input_file = "input"

if run_on_test:
    s="""x00: 1
x01: 0
x02: 1
x03: 1
x04: 0
y00: 1
y01: 1
y02: 1
y03: 1
y04: 1

ntg XOR fgs -> mjb
y02 OR x01 -> tnw
kwq OR kpj -> z05
x00 OR x03 -> fst
tgd XOR rvg -> z01
vdt OR tnw -> bfw
bfw AND frj -> z10
ffh OR nrd -> bqk
y00 AND y03 -> djm
y03 OR y00 -> psh
bqk OR frj -> z08
tnw OR fst -> frj
gnj AND tgd -> z11
bfw XOR mjb -> z00
x03 OR x00 -> vdt
gnj AND wpb -> z02
x04 AND y00 -> kjc
djm OR pbm -> qhw
nrd AND vdt -> hwm
kjc AND fst -> rvg
y04 OR y02 -> fgs
y01 AND x02 -> pbm
ntg OR kjc -> kwq
psh XOR fgs -> tgd
qhw XOR tgd -> z09
pbm OR djm -> kpj
x03 XOR y03 -> ffh
x00 XOR y04 -> ntg
bfw OR bqk -> z06
nrd XOR fgs -> wpb
frj XOR qhw -> z04
bqk OR frj -> z07
y03 OR x01 -> nrd
hwm AND bqk -> z03
tgd XOR rvg -> z12
tnw OR pbm -> gnj"""
else:
    with open(input_file) as f:
        s=f.read()

# parse lines
s1, s2 = s.strip().split('\n\n')
v={}
for x in s1.strip().split('\n'):
    s, val = x.split(':')
    v[s] = int(val)

ops = {}
op_fs = {
    'OR':  lambda x,y: x|y,
    'AND': lambda x,y: x&y,
    'XOR': lambda x,y: x^y,
}
no_deps = set()
deps = defaultdict(set)
parents = defaultdict(set)
n_deps = {}
max_z = 0
xs = []
zs = []
for x in s2.strip().split('\n'):
    n1, op, n2, _, n3 = x.split()
    if n1 > n2:
        n1, n2 = n2, n1
    ops[n3] = (n1, op, n2)
    if n1 in v and n2 in v:
        no_deps.add(n3)
    deps[n2].add(n3)
    deps[n1].add(n3)
    parents[n3].add(n1)
    parents[n3].add(n2)
    n_deps[n3] = 2-sum((n1 in v, n2 in v))
    if n3[0] == 'z':
        max_z = max(max_z, int(n3[1:]))

    # diagnosics
    if 'x' in n1 or 'y' in n1:
        # if 'y' in n1:
        #     n1, n2 = n2, n1
        xs.append((n1, op, n2, n3))
    if 'z' in n3:
        zs.append((n3, n1, op, n2))
for x in sorted(xs):
    n1, op, n2, n3 = x
    #print(n1, op, n2, n3)
for x in sorted(zs):
    n3, n1, op, n2 = x
    #print(n3, n1, op, n2)
while no_deps:
    n3 = no_deps.pop()
    n1, op, n2 = ops[n3]
    v[n3] = op_fs[op](v[n1], v[n2])
    for n in deps[n3]:
        n_deps[n] -= 1
        if not n_deps[n]:
            no_deps.add(n)

Z = 0
z = ''
for i in reversed(range(max_z+1)):
    Z += v[f'z{str(i).zfill(2)}']<<i
    z += str(v[f'z{str(i).zfill(2)}'])
u.print_copy(Z)

# too low: 16225872389232

# problem 2
node_roles = defaultdict(set)
switch_cands = defaultdict(set)
for i in range(45):
    # check for all X's
    istr = str(i).zfill(2)
    x = f'x{str(i).zfill(2)}'
    y = f'y{str(i).zfill(2)}'
    z = f'z{str(i).zfill(2)}'
    zp = f'z{str(i+1).zfill(2)}'

    # - paired with Y's twice,
    seen_ops = set()

    for o in deps[y]:
        n1, op, n2 = ops[o]
        seen_ops.add(op)
        if not(n1 == x):
            # all gates must pair with y
            print('Not matched with X!', x, y, o, ops[o])

    for o in deps[x]:
        n1, op, n2 = ops[o]
        seen_ops.add(op)
        if not(n2 == y):
            # all gates must pair with y
            print('Not matched with Y!', x, y, o, ops[o])

        if op == 'XOR' and i > 0:
            # one dep must be xor with remainder i-1 giving z
            # the other must be and with remainder i - 1 as input to R i
            node_roles[o].add((f'xy_xor_{istr}', ...))
            if not len(deps[o]) == 2:
                print('Too few deps', x, op, deps[0], o)
                switch_cands[o].add(f'too few deps as xy_or_{istr}')

            for do in deps[o]:
                dn1, dop, dn2 = ops[do]
                if dn1 != o:
                    dn1, dn2 = o, dn1
                if dop == 'XOR':
                    node_roles[dn2].add( (f'R{str(i-1).zfill(2)}', 'from xor-xor'))
                    node_roles[do].add ((f'z{istr}', 'from xor-xor'))
                    if 'z' not in do: switch_cands[do].add(f'should be z{istr} for xor/xor but is not')
                elif dop == 'AND':
                    node_roles[dn2].add((f'R{str(i - 1).zfill(2)}', 'from xor-and'))
                    node_roles[do].add((f'R-dep input to R{istr}', 'from xor-and'))
                    for ddo in deps[do]:
                        ddn1, ddop, ddn2 = ops[ddo]
                        node_roles[ddo].add((f'R{istr}', 'from xor-and-or'))
        if op == 'AND' and i > 1:
            node_roles[o].add(f'xy_and_{str(i).zfill(2)}')
            # only dep must be R i
            if not len(deps[o]) == 1:
                switch_cands[o].add(f'too many deps as xy_and_{istr}')
                print(x, op)

            for do in deps[o]:
                dn1, dop, dn2 = ops[do]
                if dn1 != o:
                    dn1, dn2 = o, dn1
                node_roles['dn2'].add((f'R{istr}', 'from and-or'))
                for ddo in deps[do]:
                    ddn1, ddop, ddn2 = ops[ddo]
                    if ddop == 'XOR':
                        if not 'z' in ddo: switch_cands[ddo].add(f'should be z{str(i+1).zfill(2)} for and-or-xor but is not')
    if not seen_ops == {'AND', 'XOR'}:
        # there must be an
        print('Missing either AND or XOR for: ', x, y, o)
    # - proceding to correct
    # - identify remainder terms
    # - proceding to
    ...

    nz1, opz, nz2 = ops[z]
    if not opz == 'XOR': switch_cands[z].add(f'supposedly z{istr}, but is NOT made from XOR')


print(len(switch_cands))
for k in switch_cands:
    print(k, switch_cands[k])
u.print_copy(','.join(sorted([k for k in switch_cands])))

# wrong answer: gst,khg,nhn,rcb,tvb,vdc,z12,z25
# right answer: gst,khg,nhn,tvb,vdc,z12,z21,z33