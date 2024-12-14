import sys
import re
import itertools

sys.setrecursionlimit(10**6)

WIDTH = 101
HEIGHT = 103
TIME = 100

QUADRANTS = [(0, 49, 0, 50), (51, 100, 0, 50), (0, 49, 52, 102), (51, 100, 52, 102)]



def main(file):
    bots0 = read_data(file)
    bots1 = []
    for p, v in bots0:
        x = (p[0] + TIME * v[0]) % WIDTH
        y = (p[1] + TIME * v[1]) % HEIGHT
        bots1.append((x, y))
    # for bot in bots1:
    #     print(bot)
    # print()
    counts = [0,0,0,0]
    for x, y in bots1:
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
    print(total)




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
