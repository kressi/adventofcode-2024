import sys
import re
import itertools

sys.setrecursionlimit(100000)

def main(file):
    with open(file) as f:
        lines = f.read().splitlines()
    total = 0
    for line in lines:
        res, numbers = line.split(":")
        res = int(res)
        numbers = numbers.split()
        n = len(numbers) - 1
        # perms = itertools.permutations(["*", "+"] * n, n)
        prod = itertools.product(["*", "+"], repeat = n)
        # print(numbers)
        for operators in prod:
            # print(operators)
            res_2 = int(numbers[0])
            for o, n in zip(operators, numbers[1:]):
                # print(res_2, o, n)
                if o == "+":
                    res_2 += int(n)
                if o == "*":
                    res_2 *= int(n)
            if res_2 == res:
                total += res
                break
    print(total)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main('input')
