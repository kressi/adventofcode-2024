import sys
import re
import itertools

sys.setrecursionlimit(10**6)

#
# +---+---+---+
# | 7 | 8 | 9 |  7: 0,0 (a)
# +---+---+---+
# | 4 | 5 | 6 |
# +---+---+---+
# | 1 | 2 | 3 |   2: 2,1 (b)
# +---+---+---+
#     | 0 | A |
#     +---+---+
#
#     +---+---+
#     | ^ | A |
# +---+---+---+
# | < | v | > |
# +---+---+---+

NUM_PAD = {
    "7": (0,0),
    "8": (0,1),
    "9": (0,2),
    "4": (1,0),
    "5": (1,1),
    "6": (1,2),
    "1": (2,0),
    "2": (2,1),
    "3": (2,2),
    "_": (3,0),
    "0": (3,1),
    "A": (3,2),
}

KEY_PAD = {
    "_": (0,0),
    "^": (0,1),
    "A": (0,2),
    "<": (1,0),
    "v": (1,1),
    ">": (1,2),
}


def main(file):
    codes = read_data(file)
    total = 0
    for num, code in codes:
        l1_presses = presses_pad(code, NUM_PAD, True)
        l2_presses = []
        for p in l1_presses:
            l2_presses += presses_pad(p, KEY_PAD, True)
        l3_presses = []
        for p in l2_presses:
            l3_presses += presses_pad(p, KEY_PAD)

        m = sys.maxsize
        for p in l3_presses:
            if len(p) < m:
                m = len(p)
        total += num * m

        # print()
        print(m, "".join(code))
        # print("level 1")
        # for p in l1_presses:
        #     print(len(p), "".join(p))
        # print("level 2")
        # for p in l2_presses:
        #     print(len(p), "".join(p))
        # print("level 3")
        # for p in l3_presses:
        #     print(len(p), "".join(p))
    print(total)


def presses_pad(code, pad, permutate=False):
    sequences0 = [tuple()]
    p0 = pad["A"]
    zero = pad["_"]
    for c in code:
        p1 = pad[c]
        sequences1 = []
        for s in sequences0:
            for p in pad_presses_ab(p0, p1, zero, permutate):
                sequences1.append(s + p)
        sequences0 = sequences1
        p0 = p1
    return sequences0


# Move from a to b on num/key pad
def pad_presses_ab(a, b, zero, permutate=False):
    di = b[0] - a[0]
    dj = b[1] - a[1]
    if di > 0:
        i = tuple(["v"]) * di
    elif di < 0:
        i = tuple(["^"]) * (-di)
    else:
        i = tuple()
    if dj > 0:
        j = tuple([">"]) * dj
    elif dj < 0:
        j = tuple(["<"]) * (-dj)
    else:
        j = tuple()
    if a[0] == zero[0] and b[1] == zero[1]:
        return [i + j + tuple(["A"])]
    if a[1] == zero[1] and b[0] == zero[0]:
        return [j + i + tuple(["A"])]
    if permutate and i and j:
        return [i + j + tuple(["A"]), j + i + tuple(["A"])]
    return [i + j + tuple(["A"])]


def read_data(file):
    with open(file) as f:
        tmap = f.read().splitlines()
    nums = [int(line[0:3]) for line in tmap]
    seqs = [[c for c in line] for line in tmap]
    return zip(nums, seqs)



if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main('input')
