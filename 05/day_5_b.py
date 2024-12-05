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
            continue
        # print(pages)
        new_pages = swap(pages, rules)
        # print(new_pages)
        total += new_pages[int(len(pages)/2)]
    print(total)

def check(pages, rules):
    for rule in rules:
        left_i = find_last(rule[0], pages)
        right_i = find_first(rule[1], pages)
        if left_i > right_i:
            return False
    return True

def swap(pages, rules):
    for rule in rules:
        left_i = find_last(rule[0], pages)
        right_i = find_first(rule[1], pages)
        while left_i > right_i:
            tmp = pages[left_i]
            pages[left_i] = pages[right_i]
            pages[right_i] = tmp
            left_i = find_last(rule[0], pages)
            right_i = find_first(rule[1], pages)
    if check(pages, rules):
        return pages
    return swap(pages, rules)

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
