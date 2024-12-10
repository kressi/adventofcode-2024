import sys
import re
import itertools

sys.setrecursionlimit(10**6)

DIRECTIONS = [(1,0), (-1,0), (0,1), (0,-1)]

def main(file):
    tmap = read_data(file)
    total = 0
    for i, line in enumerate(tmap):
        for j, h in enumerate(line):
            if h == 0:
                scores = list(itertools.chain.from_iterable([score(tmap, i, j, d) for  d in DIRECTIONS]))
                # print(i, j, h, list(scores))
                # print(remove_dups(scores))
                total += len(remove_dups(scores))
    print(total)

def remove_dups(points):
    i = 0
    while i < len(points):
        e = points[i]
        j = i+1
        while j < len(points):
            if points[i] == points[j]:
                points.pop(j)
            else:
                j += 1
        i += 1
    return points

def score(tmap, i0, j0, d):
    i1 = i0 + d[0]
    j1 = j0 + d[1]
    if not in_field(tmap, i1, j1):
        return []
    h0 = tmap[i0][j0]
    h1 = tmap[i1][j1]
    if h0 + 1 != h1:
        return []
    # print()
    # print("i0:", i0, "j0:", j0, "h0:", h0)
    # print("i1:", i1, "j1:", j1, "h1:", h1)
    if h1 == 9:
        return [(i1, j1)]
    return itertools.chain.from_iterable([score(tmap, i1, j1, d) for  d in DIRECTIONS])

def in_field(tmap, i, j):
    return i >= 0 and i < len(tmap) and j >= 0 and j < len(tmap[0])

def read_data(file):
    with open(file) as f:
        tmap = f.read().splitlines()
    return [[int(h) for h in line] for line in tmap]



if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main('input')
