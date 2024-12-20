import sys
import re
import itertools

sys.setrecursionlimit(10**6)

DIRECTIONS = [(1,0), (-1,0), (0,1), (0,-1)]

WALL = "#"
START = "S"
END = "E"
EMPTY = "."
MIN_SAVE = 100

def main(file):
    field = read_data(file)
    s = find(field, START)
    e = find(field, END)
    nodes_fwd = create_nodes(field, s, e)
    nodes_back = create_nodes(field, e, s)
    cost_fwd = traverse(nodes_fwd, e, traverse_all=True)
    cost_back = traverse(nodes_back, s, traverse_all=True)
    print("cost start to end", cost_fwd)
    print("cost end to start", cost_back)
    walls = find_all(field, WALL)
    max_cost = cost_fwd - MIN_SAVE
    total = 0
    saves = {}
    for n0 in find_visited(nodes_fwd, max_cost=max_cost):
        _, _, n0_c = nodes_fwd[n0]
        wall_neighbors = find_neighbors(n0, walls)
        if not wall_neighbors:
            continue
        visited_x = find_visited(nodes_back, max_cost=max_cost - n0_c)
        for n1 in wall_neighbors:
            for n2 in find_neighbors(n1, visited_x):
                if n2 == n0:
                    continue
                _, _, n2_c = nodes_back[n2]
                tot_cost = n0_c + n2_c + 2
                if tot_cost <= max_cost:
                    total += 1
                    if tot_cost in saves:
                        saves[tot_cost] = saves[tot_cost] + 1
                    else:
                        saves[tot_cost] = 1

    print()
    for k, v in saves.items():
        print(f"{v} cheats save {k} picoseconds")

    print()
    print("total", total)


def find_neighbors(x, coll):
    n = []
    for d in DIRECTIONS:
        i, j = x[0] + d[0], x[1] + d[1]
        if (i, j) in coll:
            n.append((i, j))
    return n

def find_visited(nodes, max_cost=sys.maxsize):
    visited = []
    for k, v in nodes.items():
        if v[1] and v[2] <= max_cost:
            visited.append(k)
    return visited


def create_nodes(field, s, e):
    nodes = {s: (None, False, 0)}  # (predecessor, visited, cost)
    nodes[e] = (None, False, sys.maxsize)
    for x in find_all(field, EMPTY):
        nodes[x] = (None, False, sys.maxsize)
    return nodes


def traverse(nodes, e, traverse_all=True, max_cost=sys.maxsize):
    n = next_node(nodes)
    while True:
        if traverse_all:
            if n is None:
                break
        elif n is None:
            break
        elif nodes[n][2] > max_cost:
            break
        elif nodes[e][2] < sys.maxsize:
            break

        pn, vn, cn = nodes[n]
        for x in [y for y in [(n[0] + d[0], n[1] + d[1]) for d in DIRECTIONS] if y in nodes.keys()]:
            px, vx, cx = nodes[x]
            c1 = cn + 1
            if c1 < cx:
                nodes[x] = (n, vx, c1)
        nodes[n] = (pn, True, cn)
        n = next_node(nodes)

    return nodes[e][2]


def next_node(nodes):
    c = sys.maxsize
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


def read_data(file):
    with open(file) as f:
        tmap = f.read().splitlines()
    return [[c for c in line] for line in tmap]



if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main('input')
