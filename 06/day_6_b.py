import sys
import re

sys.setrecursionlimit(100000)

UP_I = 2
RIGHT_I = 3
DOWN_I = 5
LEFT_I = 7

UP = "^"
RIGHT = ">"
DOWN = "v"
LEFT = "<"

DIRECTIONS = {UP: UP_I, RIGHT: RIGHT_I, DOWN: DOWN_I, LEFT: LEFT_I}
DIRECTIONS_M = {UP: (-1,0), RIGHT: (0, 1), DOWN: (1, 0), LEFT: (0, -1)}

def main(file):
    with open(file) as f:
        lines = f.read().splitlines()
    i, j = find_pos(lines)
    print("Start: ", i, j)
    height = len(lines)
    width = len(lines[0])
    total = 0
    for k, line in enumerate(lines):
        for l, char in enumerate(line):
            if char == ".":
                visited = [[1 for x in range(width)] for y in range(height)]
                # print("obstruction: ", k, l)
                if traverse(lines, visited, i, j, lines[i][j], k, l):
                    # print("has looped")
                    total += 1
    print(total)

def find_pos(field):
    for i, line in enumerate(field):
        for j, char in enumerate(line):
            if char in DIRECTIONS.keys():
                return i, j

def traverse(field, visited, i, j, d, k, l):
    # for x, line in enumerate(field):
    #     print("".join([c if i != x or j != y else d for y, c in enumerate(line)]))
    if has_visited(visited, i, j, d):
        # print("has loop")
        return True
    visit(visited, i, j, d)
    d_i, d_j = DIRECTIONS_M[d]
    n_i = i + d_i
    n_j = j + d_j
    if leaves_field(field, n_i, n_j):
        # print("leaves field")
        return False
    if (n_i != k or n_j != l) and can_move(field, n_i, n_j):
        return traverse(field, visited, n_i, n_j, d, k, l)
    else:
        return traverse(field, visited, i, j, turn(d), k, l)

def can_move(field, i, j):
    if i < 0 or i >= len(field) or j < 0 or j >= len(field[0]):
        return False
    return not field[i][j] == "#"

def leaves_field(field, i, j):
    return i < 0 or i >= len(field) or j < 0 or j >= len(field[0])




def has_visited(visited, i, j, d):
    return (visited[i][j] % DIRECTIONS[d]) == 0

def visit(visited, i, j, d):
    # print("visit: ", i, j, d)
    visited[i][j] *= DIRECTIONS[d]

def turn(d):
    if d == UP:
        return RIGHT
    if d == RIGHT:
        return DOWN
    if d == DOWN:
        return LEFT
    if d == LEFT:
        return UP


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main('input')