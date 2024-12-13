import sys
import re
import itertools

from sympy.solvers import solve
from sympy import Symbol

sys.setrecursionlimit(10**6)

#
# Button A: X+94, Y+34
# Button B: X+22, Y+67
# Prize: X=8400, Y=5400
#
# m*x_a + n*x_b = x
# m*y_a + n*y_b = y
# cost = 3 * m + n
#


def main(file):
    machines = read_data(file)
    increase = 10_000_000_000_000
    total = 0
    for a, b, p in machines:
        cost = find_min(a, b, (p[0]+increase, p[1]+increase))
        if not cost is None:
            total += cost
    print(total)

def find_min(a, b, p):
    # print()
    # print("a    ", a)
    # print("b    ", b)
    # print("prize", p)

    n = Symbol("n", integer=True)
    m = Symbol("m", integer=True)
    s = solve([m*a[0] + n*b[0] - p[0], m*a[1] + n*b[1] - p[1]], [m,n])
    if s:
        print(s)
        return 3 * s[m] + s[n]


def limit_press(btn, prize):
    min_p = min(int(prize[0]/btn[0]), int(prize[1]/btn[1]))
    max_p = max(int(prize[0]/btn[0]), int(prize[1]/btn[1])) + 2
    return (min_p, max_p)

# Button A: X+94, Y+34
# Button B: X+22, Y+67
# Prize: X=8400, Y=5400
def read_data(file):
    with open(file) as f:
        machines0 = f.read().split("\n\n")
    machines1 = [[match_x_y(line) for line in m0.splitlines()] for m0 in machines0]
    return machines1

def match_x_y(line):
    matches = re.findall(r'.*X(?:=|\+)(\d+), Y(?:=|\+)(\d+)', line)
    return (int(matches[0][0]), int(matches[0][1]))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main('input')
