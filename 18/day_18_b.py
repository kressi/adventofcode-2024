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

# GRID_MAX = 6
GRID_MAX = 70
NUM_BYTES = 1024


def main(file):
    field = read_data(file)
    s = (0,0)
    e = (GRID_MAX, GRID_MAX)

    #
    # ok:
    # - 2500
    #
    # failing:
    # - 3000
    #
    falling_bytes = 2898

    while True or falling_bytes > len(field):

        nodes = {}
        for i in range(GRID_MAX + 1):
            for j in range(GRID_MAX + 1):
                nodes[(i,j)] = (None, False, sys.maxsize)
        nodes[s] = (None, False, 0)  # (predecessor, visited, cost)

        q = None
        for i, q in enumerate(field):
            if i >= falling_bytes:
                break
            if q in nodes:
                nodes.pop(q)

        n = next_node(nodes)
        while not n is None and nodes[e][2] >= sys.maxsize:
            pn, vn, cn = nodes[n]
            nxts = [x for x in [(n[0] + d[0], n[1] + d[1]) for d in DIRECTIONS] if x in nodes.keys()]
            for x in nxts:
                px, vx, cx = nodes[x]
                c1 = cn + 1
                if c1 < cx:
                    nodes[x] = (n, vx, c1)
            nodes[n] = (pn, True, cn)
            n = next_node(nodes)

        print(falling_bytes, q, nodes[e])

        if nodes[e][2] >= sys.maxsize:
            print("reached end")
            break

        falling_bytes += 1


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


def in_field(field, i, j):
    return i >= 0 and i < len(field) and j >= 0 and j < len(field[0])


def read_data(file):
    with open(file) as f:
        tmap = f.read().splitlines()
    return [to_tuple(line) for line in tmap]

def to_tuple(line):
    x, y = line.split(",")
    return (int(x), int(y))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main('input')
