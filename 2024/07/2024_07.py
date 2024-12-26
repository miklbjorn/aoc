from functools import reduce

run_on_test = False
input_file = "test_input" if run_on_test else "input"

lines = []
with open(input_file) as f:
    for l in f.readlines():
        target, rest = l.split(':')
        numbers = list(map(lambda x: int(x), rest.strip().split(' ')))
        lines.append((int(target), numbers))

# problem 1
def is_valid(line, get_options_func):
    target, numbers = line
    N = len(numbers)
    def _check(current_val, index):
        if current_val > target:
            return False
        options = get_options_func(current_val, numbers, index)
        if index == N - 1:
            return target in options
        return any(_check(o, index+1) for o in options)

    return _check(numbers[0], 1)

def options_part_1(current_val, numbers, index):
    return [
        current_val + numbers[index],
        current_val * numbers[index],
    ]

print(
    reduce(
        lambda x, y: (x[0]+y[0],),
        filter(lambda l: is_valid(l, options_part_1), lines)
    )[0]
)
#problem 2
def options_part_2(current_val, numbers, index):
    return [
        current_val + numbers[index],
        current_val * numbers[index],
        int(str(current_val) + str(numbers[index])),
    ]

print(
    reduce(
        lambda x, y: (x[0]+y[0],),
        filter(lambda l: is_valid(l, options_part_2), lines)
    )[0]
)

