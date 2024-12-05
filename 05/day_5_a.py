import sys
import re

def main(file):
    with open(file) as f:
        a, b = f.read().split("\n\n")
    rules = []
    for i in a.splitlines():
        x, y = i.split("|")
        rules.append((int(x), int(y)))
    pages_stack = []
    for i in b.splitlines():
        pages_stack.append([int(x) for x in i.split(",")])
    total = 0
    for pages in pages_stack:
        if check(pages, rules):
            total += pages[int(len(pages)/2)]
    print(total)

def check(pages, rules):
    for rule in rules:
        left_i = find_last(rule[0], pages)
        right_i = find_first(rule[1], pages)
        if left_i > right_i:
            return False
    return True

def find_last(num, pages):
    match = -1
    for i, page in enumerate(pages):
        if page == num:
            match = i
    return match

def find_first(num, pages):
    for i, page in enumerate(pages):
        if page == num:
            return i
    return len(pages)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main('input')
