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
    total = len(antinodes0)
    print(total)

def antinodes(antennas, size):
    non_super = [(i, j) for j in range(size[1]) for i in range(size[0])]
    print(non_super)
    super_nodes = []
    for a, nodes in antennas.items():
        if len(nodes) < 2:
            continue
        pairs = itertools.combinations(nodes, 2)
        for p in pairs:
            for i, n in enumerate(non_super):
                if colinear(p[0], p[1], n):
                    super_nodes.append(n)
                    non_super.pop(i)
    return super_nodes

def colinear(a, b, c):
    return a[0] * (b[1] - c[1]) + b[0] * (c[1] - a[1]) + c[0] * (a[1] - b[1]) == 0

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main('input')
