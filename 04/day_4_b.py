import sys
import re

def main(file):
    with open(file) as f:
        lines = f.read().splitlines()
    print(count_xmas(lines))

def count_xmas(field):
    total = 0
    for i, line in enumerate(field):
        for j, char in enumerate(line):
            if char == "A":
                total += count_from(i, j, field)
    return total

def count_from(i, j, field):
    max_i = len(field)
    max_j = len(field[0])
    if i - 1 < 0 or i + 1 >= max_i or j - 1 < 0 or j + 1 >= max_j:
        return 0
    d_1 = (field[i-1][j-1], field[i+1][j+1])
    d_2 = (field[i-1][j+1], field[i+1][j-1])
    if (d_1 == ("M", "S") or d_1 == ("S", "M")) and (d_2 == ("M", "S") or d_2 == ("S", "M")):
        return 1
    return 0

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main('input')
