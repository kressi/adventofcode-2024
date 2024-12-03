import sys
import re

def main(file):
    with open(file) as f:
        t = f.read()
    total = 0
    do = True
    for term in re.finditer(r'(?:mul\((\d{1,3}),(\d{1,3})\))|(?:do\(\))|(?:don\'t\(\))', t):
        print(term.group(0))
        if term.group(0) == "don't()":
            do = False
        elif term.group(0) == "do()":
            do = True
        elif do:
            total += int(term.group(1)) * int(term.group(2))
    print(total)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main('input')
