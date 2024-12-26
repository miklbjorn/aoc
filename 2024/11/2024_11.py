import utils as u
from functools import reduce, cache

run_on_test = False
input_file = "test_input" if run_on_test else "input"

if run_on_test:
    s="""125 17"""
else:
    with open(input_file) as f:
        s=f.read()

stones = [str(x) for x in s.strip().split()]

@cache
def _get_n_stones(stone, n_iters):
    if n_iters <= 0: return 1
    if stone == 0:
        return _get_n_stones(1, n_iters - 1)
    str_stone = str(stone)
    if (n :=len(str_stone)) % 2 == 0:
        st1, st2 = int(str_stone[:n//2]), int(str_stone[n//2:])
        return _get_n_stones(st1, n_iters - 1) + _get_n_stones(st2, n_iters - 1)
    return _get_n_stones(stone * 2024, n_iters-1)


sum1, sum2 = 0, 0
for stone in stones:
    sum1 += _get_n_stones(int(stone), 25)
    sum2 += _get_n_stones(int(stone), 75)
print(sum1)
print(sum2)

# outdated part 1 solution
# cache2 = {}
# def _update(stone):
#     if stone in cache2:
#         return cache2[stone]
#     if stone == '0':
#         cache2[stone] = ['1']
#         return cache2[stone]
#     if len(stone) % 2 == 0:
#         n = len(stone)
#         cache2[stone] =[stone[:n//2], str(int(stone[n//2:]))]
#         return cache2[stone]
#     cache2[stone] = [str(int(stone)*2024)]
#     return  cache2[stone]
#
# for i in range(25):
#     print(i)
#     # print(stones)
#     #stones = list(reduce(lambda x, y: x + y,map(_update, stones)))
