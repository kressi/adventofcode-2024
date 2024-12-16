import sys
import re
import itertools

sys.setrecursionlimit(10**6)

EAST  = ( 0, 1)
WEST  = ( 0,-1)
NORTH = (-1, 0)
SOUTH = ( 1, 0)

DIRECTIONS = [EAST, WEST, NORTH, SOUTH]

WALL = "#"
START = "S"
END = "E"
EMPTY = "."
MIN = 10**7


def main(file):
    field = read_data(file)
    s = find(field, START)
    e = find(field, END)

    nodes = {}
    for x in find_all(field, EMPTY) + [s, e]:
        for d in DIRECTIONS:
            if field[x[0] - d[0]][x[1] - d[1]] == WALL:
                continue
            nodes[(x, d)] = ([], False, MIN)  # (predecessor, visited, cost)
    nodes[(s, EAST)] = ([], False, 0)

    # print()
    # for k, v in nodes.items():
    #     print(k, v)

    k = next_node(nodes)
    while not k is None:
        n, d = k
        pn, _, cn = nodes[(n, d)]
        for dx in DIRECTIONS:
            if d[0] == -dx[0] and d[1] == -dx[1]:
                continue
            nx = (n[0]+dx[0], n[1]+dx[1])
            if not (nx, dx) in nodes.keys():
                continue
            px, vx, cx = nodes[(nx, dx)]
            c1 = cn + 1
            if d != dx:
                c1 += 1000
            if c1 < cx:
                nodes[(nx, dx)] = ([k], vx, c1)
            elif c1 == cx:
                nodes[(nx, dx)] = (px + [k], vx, c1)
        nodes[k] = (pn, True, cn)
        # print()
        # for k, v in nodes.items():
        #     print(k, v)
        k = next_node(nodes)

    for k in [x for x in nodes.keys() if x[0] == e]:
        print(k, nodes[k])
        tiles = find_all(field, EMPTY) + [s, e]
        print(reverse(nodes, k, tiles))


def reverse(nodes, k0, tiles):
    total = 0
    n0, d0 = k0
    if n0 in tiles:
        total += 1
        i = tiles.index(n0)
        tiles.pop(i)
    n1 = (n0[0] - d0[0], n0[1] - d0[1])
    for ki in nodes[k0][0]:
        total += reverse(nodes, ki, tiles)
    return total



def calc_dir(a, b):
    return (b[0] - a[0], b[1] - a[1])

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
