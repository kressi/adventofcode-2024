import sys
import re
import itertools

sys.setrecursionlimit(10**6)


def main(file):
    numbers = read_data(file)
    # numbers = [123]
    total = 0
    for secret in numbers:
        s0 = secret
        # print()
        for _ in range(2000):
            # print(s0)
            s1 = next_secret(s0)
            s0 = s1
        total += s0
        # print(secret, s0)
    print(total)


def next_secret(secret):
    p0 = secret * 64
    s0 = mix_prune(p0, secret)
    p1 = s0 // 32
    s1 = mix_prune(p1, s0)
    p2 = s1 * 2048
    s2 = mix_prune(p2, s1)
    return s2


def mix_prune(a, b):
    return (a ^ b) % 16_777_216


def read_data(file):
    with open(file) as f:
        tmap = f.read().splitlines()
    return [int(line) for line in tmap]



if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main('input')
