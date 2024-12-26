import utils as u

run_on_test = False
input_file = "test_input" if run_on_test else "input"

if run_on_test:
    s="""2333133121414131402
    """
else:
    with open(input_file) as f:
        s=f.read()


full_list = []
ds = [int(c) for c in s.strip()]
files = []
empty_spans = []
for i, d in enumerate(ds):
    if i % 2 == 0:
        val = i//2
        # (id, blocks, start, end)
        files.append([val, d, len(full_list), len(full_list)+d])
    else:
        val = -1
        empty_spans.append([val, d, len(full_list), len(full_list) + d])
    full_list += [val]*d

sum = 0
N = len(full_list)
j = N - 1
og_full_list = full_list.copy()
for i, v in enumerate(full_list):
    if v >= 0:
        pass
    else:
        while (v := full_list[j]) < 0:
            j = j-1
        if i >= j:
            break
        full_list[i], full_list[j] = full_list[j], full_list[i]
    #
    sum += i * int(v)

u.print_copy(sum)

# problem 2
full_list = og_full_list
def _move(file, span):
    if span[1] < file[1]: raise
    full_list[span[2]:span[2]+file[1]] = [file[0]]*file[1]
    full_list[file[2]:file[3]] = [span[0]]*file[1]
    span[1] = span[1] - file[1]
    span[2] = span[2] + file[1]

for f in reversed(files):
    for e in empty_spans:
        if e[2] >= f[2]:
            break
        if e[1] >= f[1]:
            _move(f, e)
            break

sum = 0
for i, v in enumerate(full_list):
    if v > 0:
        sum += i * v

u.print_copy(sum)
