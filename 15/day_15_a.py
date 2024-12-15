import sys
import re
import itertools

sys.setrecursionlimit(10**6)

BOX = "O"
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
    for m in moves:
        b = find_bot(field)
        move(field, b, DIRECTIONS[m])
        # print()
        # for line in field:
        #     print("".join(line))
    print(score(field))


def find_bot(field):
    for i, line in enumerate(field):
        for j, c in enumerate(line):
            if c == BOT:
                return (i, j)


def move(field, b, d):
    r = 0
    p = None
    can_move = False
    while True:
        r += 1
        p = (b[0] + r * d[0], b[1] + r * d[1])
        if field[p[0]][p[1]] == BOX:
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



def score(field):
    total = 0
    for i, line in enumerate(field):
        for j, c in enumerate(line):
            if c != BOX:
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
