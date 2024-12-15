import sys
import re
import itertools

sys.setrecursionlimit(10**6)

BOX = "O"
BOX_L = "["
BOX_R = "]"
BOX_J = {
    BOX_L: 1,
    BOX_R: -1,
}
WALL = "#"
BOT = "@"
EMPTY = "."

DIRECTIONS = {
    "^": (-1, 0),
    "v": ( 1, 0),
    ">": ( 0, 1),
    "<": ( 0,-1),
}

def main(file):
    field, moves = read_data(file)
    for line in field:
        print("".join(line))
    field = inflate(field)
    for line in field:
        print("".join(line))
    for m in moves:
        b = find_bot(field)
        d = DIRECTIONS[m]
        if d[0] == 0:
            move_h(field, b, d)
        else:
            move_v(field, b, d)
        print()
        print("Move", m, d)
        for line in field:
            print("".join(line))
    print(score(field))


def inflate(field):
    return [ list(itertools.chain.from_iterable([char_map(c) for c in line])) for line in field]

def char_map(c):
    if c in [EMPTY, WALL]:
        return [c] * 2
    if c == BOT:
        return [BOT, EMPTY]
    if c == BOX:
        return [BOX_L, BOX_R]
    assert False


def find_bot(field):
    for i, line in enumerate(field):
        for j, c in enumerate(line):
            if c == BOT:
                return (i, j)


def move_h(field, b, d):
    r = 0
    p = []
    can_move = False
    while True:
        r += 1
        p = (b[0] + r * d[0], b[1] + r * d[1])
        if field[p[0]][p[1]] in [BOX_L, BOX_R]:
            continue
        if field[p[0]][p[1]] == WALL:
            break
        if field[p[0]][p[1]] == EMPTY:
            can_move = True
            break
        print("bot", b)
        print("r  ", r)
        print("d  ", d)
        print("p  ", p)
        print("   ", field[p[0]][p[1]])
        assert False
    if can_move:
        for s in range(r, 0, -1):
            p0 = (b[0] + (s-1) * d[0], b[1] + (s-1) * d[1])
            p1 = (b[0] +     s * d[0], b[1] +     s * d[1])
            field[p1[0]][p1[1]] = field[p0[0]][p0[1]]
            field[p0[0]][p0[1]] = EMPTY


def move_v(field, b, d):
    d_i = d[0]
    ok, boxes = move_v_rec(field, [b], d_i)
    if not ok:
        return field
    for b in boxes[::-1]:
        field[b[0]+d_i][b[1]] = field[b[0]][b[1]]
        field[b[0]][b[1]] = EMPTY


def move_v_rec(field, boxes, d_i):
    for p in boxes:
        target = field[p[0]+d_i][p[1]]
        if target == WALL:
            return (False, None)
        if target == EMPTY:
            boxes.append(p)
        if target in [BOX_L, BOX_R]:
            x0 = (p[0],       p[1])
            y0 = (p[0],       p[1] + BOX_J[target])
            x1 = (p[0] + d_i, p[1])
            y1 = (p[0] + d_i, p[1] + BOX_J[target])
            ok, br = move_v_rec(field, [x1, y1], d_i)
            if not ok:
                return (False, None)
            boxes += [x0, y0] + br
    return (True, boxes)


def score(field):
    total = 0
    for i, line in enumerate(field):
        for j, c in enumerate(line):
            if c != BOX_L:
                continue
            total += 100 * i + j
    return total


def read_data(file):
    with open(file) as f:
        tmap = f.read().split("\n\n")
    field = [[c for c in line] for line in tmap[0].splitlines()]
    moves = [c for c in tmap[1] if c in DIRECTIONS.keys()]
    return (field, moves)



if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main('input')
