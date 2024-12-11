import sys
import re
import itertools

sys.setrecursionlimit(10**6)

def main(file):
    stones = read_data(file)
    total = 0
    print(stones)
    for i in range(25):
        stones = blink(stones)
        # print(stones)
    print(len(stones))


def blink(stones):
    stones2 = []
    for stone in stones:
        l = len(stone)
        if int(stone) == 0:
            stones2.append("1")
        elif l % 2 == 0:
            stones2.append(stone[:int(l/2)])
            stones2.append(str(int(stone[int(l/2):])))
        else:
            n = 2024 * int(stone)
            stones2.append(str(n))
    return stones2


def read_data(file):
    with open(file) as f:
        tmap = f.read()
    return tmap.split()



if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main('input')
