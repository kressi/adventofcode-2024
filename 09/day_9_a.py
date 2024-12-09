import sys
import re
import itertools

sys.setrecursionlimit(100_000)


def main(file):
    blocks = read_data(file)
    target = []
    while len(blocks) > 0:
        yd, l, f = blocks.pop(0)
        if l > 0:
            target.append((yd, l))
        while f > 0 and len(blocks) > 0:
            ydz, lz0, fz = blocks[-1]
            take = min(lz0, f)
            if take > 0:
                target.append((ydz, take))
            lz1 = lz0 - take
            if lz1 > 0:
                blocks[-1] = (ydz, lz1, fz)
            else:
                blocks.pop(-1)
            f = f - take
    print(target)
    print(checksum(target))

def checksum(blocks):
    total = 0
    position = 0
    for block in blocks:
        for i in range(block[1]):
            total += position * block[0]
            position += 1
    return total



def read_data(file):
    with open(file) as f:
        disk = f.read()
    # print(disk)
    disk += "0"
    blocks = [(int(i), int(disk[2*i]), int(disk[2*i + 1])) for i in range(0, int(len(disk) / 2))]
    print(blocks)
    return blocks


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main('input')
