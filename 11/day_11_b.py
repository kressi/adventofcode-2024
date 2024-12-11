import sys
import re
import itertools

from cache_a import *
from cache_b import *

sys.setrecursionlimit(10**6)



def main(file):
    stones = read_data(file)
    # for c in [10120, 12144, 14168, 16192, 18216, 20, 2024, 2048, 24, 2457, 26, 2608, 2867, 2880, 32, 3277, 32772608, 36, 3686, 40, 4048, 48, 56, 57, 6032, 72, 77, 77, 77, 77, 77, 80, 80, 80, 80, 80, 8096, 84, 86, 91, 9184, 94, 9456, 96]:
    #     for i in range(1, 50):
    #         count([str(c)], i)
    total = count(stones, 75)
    print(total)

def count(stones, iterations):
    total = 0
    for stone in stones:
        count = blink(stone, iterations)
        # print("stone:", stone,"iterations:", iterations,"count:", count)
        total += count
        # count = blink_x(stone, iterations)
        # print("stone:", stone,"iterations:", iterations,"count:", count)
    return total


def blink(stone, c):
    if c <= 0:
        return 1
    key_b  = stone + "-" + str(c)
    if key_b in CACHE_B:
        return CACHE_B[key_b]
    if stone in CACHE_A:
        cache_a = CACHE_A[stone]
        off = None
        keys_a = [x for x in cache_a.keys() if x < c]
        if keys_a:
            off = max(keys_a)
        if not off is None:
            stones_cache = cache_a[off]
            return sum([blink(s, c-off) for s in stones_cache])
    return sum([blink(s, c-1) for s in arrange(stone)])

def blink_x(stone, c):
    if c <= 0:
        return [stone]
    key_b  = stone + "-" + str(c)
    if stone in CACHE_A:
        cache_a = CACHE_A[stone]
        off = None
        keys_a = [x for x in cache_a.keys() if x < c]
        if keys_a:
            off = max(keys_a)
        if not off is None:
            stones_cache = cache_a[off]
            return list(itertools.chain.from_iterable([blink_x(s, c-off) for s in stones_cache]))
    return list(itertools.chain.from_iterable([blink_x(s, c-1) for s in arrange(stone)]))

def arrange(stone):
    l = len(stone)
    if int(stone) <= 0:
        return ["1"]
    elif l % 2 == 0:
        return [stone[:int(l/2)], str(int(stone[int(l/2):]))]
    else:
        n = 2024 * int(stone)
        return [str(n)]


def read_data(file):
    with open(file) as f:
        tmap = f.read()
    return tmap.split()



if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main('input')
