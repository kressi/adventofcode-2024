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
                scores = [score(tmap, i, j, d) for  d in DIRECTIONS]
                total += sum(scores)
    print(total)

def score(tmap, i0, j0, d):
    i1 = i0 + d[0]
    j1 = j0 + d[1]
    if not in_field(tmap, i1, j1):
        return 0
    h0 = tmap[i0][j0]
    h1 = tmap[i1][j1]
    if h0 + 1 != h1:
        return 0
    if h1 == 9:
        return 1
    return sum([score(tmap, i1, j1, d) for  d in DIRECTIONS])

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
