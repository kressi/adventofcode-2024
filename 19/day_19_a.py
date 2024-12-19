import sys
import re
import itertools

sys.setrecursionlimit(10**6)

CACHE = {}

def main(file):
    patterns, designs = read_data(file)
    total = 0
    for i, d in enumerate(designs):
        if design_ok(d, patterns, 0, 0):
            print("ok ",i, d)
            total += 1
        else:
            print("nok",i, d)
    print(total)

def design_ok(design, patterns, idx, count):
    # print()
    # print("count", count, "idx", idx, "len", len(design), design[idx:])
    key = (design[idx:])
    if key in CACHE:
        return CACHE[key]
    if idx >= len(design):
        return True
    for pattern in patterns:
        p_end = idx + len(pattern)
        if p_end > len(design):
            continue
        if design[idx:p_end] != pattern:
            continue
        # print("count", count, "idx", idx, "p_end", p_end, "len", len(design), design[idx:], design[idx:p_end], pattern)
        is_ok = design_ok(design, patterns, p_end, count+1)
        if is_ok:
            CACHE[key] = True
            return True
    CACHE[key] = False
    return False


def read_data(file):
    with open(file) as f:
        tmap = f.read().split("\n\n")
    patterns = [p for p in tmap[0].split(", ")]
    designs = tmap[1].splitlines()
    return patterns, designs


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main('input')
