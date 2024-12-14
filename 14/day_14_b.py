import sys
import re
import itertools

sys.setrecursionlimit(10**6)

WIDTH = 101
HEIGHT = 103
TIME = 100

QUADRANTS = [(0, 49, 0, 50), (51, 100, 0, 50), (0, 49, 52, 102), (51, 100, 52, 102)]
CACHE = []


def main(file):
    bots0 = read_data(file)
    for t in range(100_000):
        bots1 = move(bots0, t)
        if not bots1:
            continue
        visualize(bots1, t)
        if bots1 in CACHE:
            break
        CACHE.append(bots1)
    print(count(bots1))


def visualize(bots, t):
    field = [["." for i in range(WIDTH)] for j in range(HEIGHT)]
    for x, y in bots:
        field[y][x] = "*"
    field2 = ["", "t: " + str(t)] + ["".join(line) for line in field]
    with open("visualizations", "a") as f:
        f.write("\n".join(field2))


def move(bots0, t):
    bots1 = []
    for p, v in bots0:
        x = (p[0] + t * v[0]) % WIDTH
        y = (p[1] + t * v[1]) % HEIGHT
        if (x, y) in bots1:
            return []
        bots1.append((x, y))
    return bots1


def count(bots):
    counts = [0,0,0,0]
    for x, y in bots:
        for i, q in enumerate(QUADRANTS):
            if x < q[0] or x > q[1] or y < q[2] or y > q[3]:
                continue
            # print(x, y, q)
            counts[i] = counts[i] + 1
    # print()
    # print(counts)
    total = 1
    for count in counts:
        total = total * count
    return total



# p=0,4 v=3,-3
def read_data(file):
    with open(file) as f:
        lines = f.read().splitlines()
    bots = []
    for line in lines:
        x = re.findall(r'.*p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)', line)
        y = x[0]
        bots.append(((int(y[0]), int(y[1])), (int(y[2]), int(y[3]))))
    return bots



if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main('input')
