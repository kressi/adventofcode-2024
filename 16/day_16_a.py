import sys
import re
import itertools

sys.setrecursionlimit(10**6)

DIRECTIONS = [(1,0), (-1,0), (0,1), (0,-1)]

WALL = "#"
START = "S"
END = "E"
EMPTY = "."
MIN = 10**7


def main(file):
    field = read_data(file)
    s = find(field, START)
    e = find(field, END)
    nodes = {s: ((s[0], s[1]-1), False, 0)}  # (predecessor, visited, cost)
    nodes[e] = (None, False, MIN)
    for x in find_all(field, EMPTY):
        nodes[x] = (None, False, MIN)
    while nodes[e][2] >= MIN:
        n = next_node(nodes)
        pn, vn, cn = nodes[n]
        nxts = [x for x in [(n[0] + d[0], n[1] + d[1]) for d in DIRECTIONS] if x in nodes.keys()]
        for x in nxts:
            px, vx, cx = nodes[x]
            c1 = cn + turn(pn, n, x) * 1000 + 1
            if c1 < cx:
                nodes[x] = (n, vx, c1)
        nodes[n] = (pn, True, cn)
        # for k, v in nodes.items():
        #     print(k, v)

    print(nodes[e][2])


def turn(a, b, c):
    return 1 if c[0] - b[0] != b[0] - a[0] or c[1] - b[1] != b[1] - a[1] else 0


def next_node(nodes):
    c = MIN
    n = None
    for node, v in nodes.items():
        if v[1]:
            continue
        if v[2] < c:
            n = node
            c = v[2]
    return n



def find(field, obj):
    for i, line in enumerate(field):
        for j, c in enumerate(line):
            if c == obj:
                return (i, j)


def find_all(field, obj):
    aggr = []
    for i, line in enumerate(field):
        for j, c in enumerate(line):
            if c == obj:
                aggr.append((i,j))
    return aggr


def in_field(field, i, j):
    return i >= 0 and i < len(field) and j >= 0 and j < len(field[0])


def read_data(file):
    with open(file) as f:
        tmap = f.read().splitlines()
    return [[c for c in line] for line in tmap]



if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main('input')
