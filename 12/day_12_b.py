
import sys
import re
import itertools

sys.setrecursionlimit(10**6)


DIRECTIONS = [(0,1), (0,-1), (1,0), (-1,0)]


def main(file):
    garden = read_data(file)
    r = regions(garden)
    total = 0
    for c, points in r:
        area = len(points)
        p = perimeter(points, len(garden), len(garden[0]))
        print(c, area, p, points)
        total += area * p
    print(total)


def regions(garden):
    r = []
    for i, _ in enumerate(garden):
        for j, _ in enumerate(garden[0]):
            current = garden[i][j]
            if current == ".":
                continue
            garden[i][j] = "."
            r.append((current, [(i, j)] + list(itertools.chain.from_iterable([region(garden, current, i+dx, j+dy) for dx, dy in DIRECTIONS]))))
    return r


def region(garden, c0, i1, j1):
    if c0 == ".":
        return []
    if not in_garden(garden, i1, j1):
        return []
    if garden[i1][j1] != c0:
        return []
    garden[i1][j1] = "."
    return [(i1, j1)] + list(itertools.chain.from_iterable([region(garden, c0, i1+dx, j1+dy) for dx, dy in DIRECTIONS]))


def perimeter(points, len_i, len_j):
    total = 0
    upper_border = []  # ( 0, 1)
    lower_border = []  # ( 0,-1)
    left_border = []   # (-1, 0)
    right_border = []  # ( 1, 0)
    for i0, j0 in points:
        for di, dj in DIRECTIONS:
            i1 = i0 + di
            j1 = j0 + dj
            if (i1, j1) in points:
                continue
            if di == 0 and dj == 1:
                right_border.append((i0, j0))
            elif di == 0 and dj == -1:
                left_border.append((i0, j0))
            elif dj == 0 and di == -1:
                upper_border.append((i0, j0))
            elif dj == 0 and di == 1:
                lower_border.append((i0, j0))
            else:
                print(i0, j0, di, dj)
                assert False
    
    xi = None
    xj = None
    left_border.sort(key=second)
    #print("left ", left_border)
    for i, j in left_border:
        if j != xj or i != xi + 1:
            total += 1
        xi = i
        xj = j
    xi = None
    xj = None
    right_border.sort(key=second)
    #print("right", right_border)
    for i, j in right_border:
        if j != xj or i != xi + 1:
            total += 1
        xi = i
        xj = j
    xi = None
    xj = None
    upper_border.sort(key=first)
    #print("up   ", upper_border)
    for i, j in upper_border:
        if i != xi or j != xj + 1:
            total += 1
        xi = i
        xj = j
    xi = None
    xj = None
    lower_border.sort(key=first)
    #print("down ",lower_border)
    for i, j in lower_border:
        if i != xi or j != xj + 1:
            total += 1
        xi = i
        xj = j
    return total

def first(val):
    return val[0]*10**6+val[1]

def second(val):
    return val[1]*10**6+val[0]

def in_garden(garden, i, j):
    return i >= 0 and i < len(garden) and j >= 0 and j < len(garden[0])


def read_data(file):
    with open(file) as f:
        tmap = f.read().splitlines()
    return [[c for c in line] for line in tmap]


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main('input')
