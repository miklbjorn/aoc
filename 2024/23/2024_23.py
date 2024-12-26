import utils as u

run_on_test = False
input_file = "input"

if run_on_test:
    s="""kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn"""
else:
    with open(input_file) as f:
        s=f.read()

# parse lines
g, tns, ns = dict(), list(), list()
i = -1
for l in s.strip().split('\n'):
    n1, n2 = l.strip().split('-')
    for n in (n1, n2):
        _ns = tns if n.startswith('t') else ns
        if n not in g:
            _ns.append(n)
            g[n] = set()
    g[n1].add(n2)
    g[n2].add(n1)

ns = tns + ns
nis = {n: i for i, n in enumerate(ns)}

# problem 1: find all complete trios including element starting with n
sum = 0
for n in tns:
    i = nis[n]
    for n2 in g[n]:
        if (j := nis[n2]) < i:
            continue
        for n3 in g[n2]:
            if nis[n3] < j:
                continue
            if n in g[n3]:
                sum += 1
u.print_copy(sum)

# some diagnostics
# problem 2: maximal complete subgraph
max = 0
for n in g:
    if len(g[n]) > max:
        max = len(g[n])
print(max)

# problem 2: maximal complete subgraph
def _maximally_extend_ns(_ns, min_i):
    # return the maximal extension of the set in _ns
    # adding all nodes connected to all nodes, already in n
    # only consider nodes after index min_i in ns, the list of all nodes
    _max_ns = _ns.copy()
    for n in ns:
        if nis[n] < min_i:
            continue
        if _ns.issubset(g[n]):
            new_ns = _ns.union({n})
            new_ns = _maximally_extend_ns(new_ns, nis[n]+1)
            _max_ns = new_ns if len(new_ns) > len(_max_ns) else _max_ns
    return _max_ns

sum = 0
_max = set()
for n in ns:
    # find the maximally extended subgraph in which all nodes are connected
    # starting with each node in turn
    # only look at nodes after starting node in ordering, as all subgraphs
    # with n and a node at a lower ordering index than n will already have been checked
    i = nis[n]
    new_set = _maximally_extend_ns({n}, i + 1)
    if len(new_set) > len(_max):
        _max = new_set

u.print_copy(','.join(sorted([c for c in _max])))
