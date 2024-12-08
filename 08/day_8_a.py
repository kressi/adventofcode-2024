import sys
import re
import itertools

sys.setrecursionlimit(100000)

def main(file):
    with open(file) as f:
        lines = f.read().splitlines()
    size = (len(lines), len(lines[0]))
    antennas = {}
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char == ".":
                continue
            if char not in antennas:
                antennas[char] = []
            antennas[char].append((i, j))
    print("antennas:\n", antennas)
    antinodes0 = antinodes(antennas, size)
    print("antinodes:\n", antinodes0)
    total = 0
    for line in antinodes0:
        for n in line:
            if len(n) > 0:
                total += 1
    print(total)

def antinodes(antennas, size):
    field = [[[] for j in range(size[1])] for i in range(size[0])]
    for a, nodes in antennas.items():
        if len(nodes) < 2:
            continue
        pairs = itertools.combinations(nodes, 2)
        for p in pairs:
            for x in super(p[0], p[1], size):
                field[x[0]][x[1]].append(a)
    return field

def super(a, b, size):
    di, dj = a[0] - b[0], a[1] - b[1]
    x1 = (a[0] + di, a[1] + dj)
    x2 = (b[0] - di, b[1] - dj)
    return [x for x in [x1, x2] if x[0] >= 0 and x[0] < size[0] and x[1] >= 0 and x[1] < size[1]]

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main('input')
