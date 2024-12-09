import sys
import re
import itertools

sys.setrecursionlimit(10**6)

def main(file):
    blocks = read_data(file)
    blocks2 = defrag(blocks)
    print(checksum(blocks2))

def defrag(blocks):
    # print()
    # print(blocks)
    iz = 0
    while iz < len(blocks):
        iz += 1
        yz, lz = blocks[-iz]
        if yz is None:
            continue
        for ia in range(len(blocks)):
            if iz + ia > len(blocks):
                break
            ya, la = blocks[ia]
            if not ya is None or la < lz:
                continue
            blocks[ia] = (yz, lz)
            blocks[-iz] = (None, lz)
            lf = la - lz
            if lf > 0:
                blocks = blocks[:ia+1] + [(None, lf)] + blocks[ia+1:]
            break
        # print(blocks)
    return blocks

def checksum(blocks):
    total = 0
    position = 0
    for block in blocks:
        for i in range(block[1]):
            if not block[0] is None:
                total += position * block[0]
            position += 1
    return total

def read_data(file):
    with open(file) as f:
        disk = f.read()
    blocks = []
    for i, l in enumerate(disk):
        ii = int(i)
        li = int(l)
        yd = int(ii/2) if ii%2 == 0 else None
        if li > 0:
            blocks.append((yd, li))
    return blocks



if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main('input')
