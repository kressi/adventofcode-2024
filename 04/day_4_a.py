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
            if char == "X":
                total += count_from(i, j, field)
    return total

def count_from(i, j, field):
    max_i = len(field)
    max_j = len(field[0])
    count = 0
    for i_dir in [-1, 0, 1]:
        for j_dir in [-1, 0, 1]:
            if i_dir == 0 and j_dir == 0:
                continue
            ok = True
            for n, n_char in enumerate(["M", "A", "S"], 1):
                next_i = i + n * i_dir
                next_j = j + n * j_dir
                if next_i < 0 or next_i >= max_i:
                    ok = False
                    break
                if next_j < 0 or next_j >= max_j:
                    ok = False
                    break
                if field[next_i][next_j] != n_char:
                    ok = False
                    break
            if ok:
                count += 1
    return count

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main('input')
