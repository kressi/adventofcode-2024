import sys
import re
import itertools

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
    total = 0
    for a, b, p in machines:
        cost = find_min(a, b, p)
        if not cost is None:
            total += cost
    print(total)

def find_min(a, b, p):
    m_min = 0
    n_min = 0
    cost_min = None
    limits_a = limit_press(a, p)
    limits_b = limit_press(b, p)
    # print()
    # print("a       ", a)
    # print("limits a", limits_a)
    # print("b       ", b)
    # print("limits b", limits_b)
    # print("prize   ", p)
    for m in range(0, limits_a[1], 1):
        for n in range(0, limits_b[1], 1):
            if m * a[0] + n * b[0] != p[0] or m * a[1] + n * b[1] != p[1]:
                continue
            cost = 3 * m + n
            if cost_min is None or cost < cost_min:
                cost_min = cost
                m_min = m
                n_min = n
    return cost_min

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
