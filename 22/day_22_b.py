import sys
import re
import itertools
from collections import defaultdict

sys.setrecursionlimit(10**6)


CACHE = {}

def main(file):
    numbers = read_data(file)
    # numbers = [123]
    total = 0
    for secret_i, secret in enumerate(numbers):
        s0 = secret
        p0 = s0 % 10
        changes = []
        for _ in range(2000):
            s1 = next_secret(s0)
            p1 = s1 % 10
            change = p1 - p0
            changes.append(change)
            if p1 > 0 and len(changes) > 3:
                key = tuple(changes[-4:])
                if not key in CACHE:
                    CACHE[key] = (0, [])
                idxs = CACHE[key][1]
                if not secret_i in idxs:
                    idxs.append(secret_i)
                    CACHE[key] = (CACHE[key][0] + p1, idxs)
            s0 = s1
            p0 = p1
        total += s0
        # print(secret, s0)

    print()
    c = 0
    for k, v in sorted(CACHE.items(), key=lambda item: -item[1][0]):
        c += 1
        if c > 20:
            break
        print(k, v)
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
