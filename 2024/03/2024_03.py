import re

run_on_test = False
input_file = "test_input" if run_on_test else "input"

with open(input_file) as f:
    memory = ""
    for l in f.readlines():
        memory += l

# problem 1
def multiply_match(match):
    matches = re.findall('[0-9]+', match)
    return int(matches[0])*int(matches[1])

def run(memory):
    match_pattern="mul\([0-9]{1,3},[0-9]{1,3}\)"
    matches = re.findall(match_pattern, memory)
    print(sum(multiply_match(match) for match in matches))

run(memory)

# problem 2
dos = memory.split('do()')
new_memory = ''
for do in dos:
    new_memory += do.split("don't()")[0]
run(new_memory)