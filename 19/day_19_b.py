import sys
import re
import itertools

sys.setrecursionlimit(10**6)

CACHE = {}

def main(file):
    patterns, designs = read_data(file)
    total = 0
    for i, d in enumerate(designs):
        paths = design_ok(d, patterns, 0)
        count = paths
        print(i, "count", count, d)
        total += count
    print(total)

def design_ok(design, patterns, idx):
    # print()
    # print("count", count, "idx", idx, "len", len(design), design[idx:])
    key = (design[idx:])
    if key in CACHE:
        return CACHE[key]
    # print()
    # print(CACHE)
    if idx >= len(design):
        return 1
    paths = 0
    for i, pattern in enumerate(patterns):
        p_end = idx + len(pattern)
        if p_end > len(design):
            continue
        if design[idx:p_end] != pattern:
            continue
        paths += design_ok(design, patterns, p_end)
    CACHE[key] = paths
    return paths


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
