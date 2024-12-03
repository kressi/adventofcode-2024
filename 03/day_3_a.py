import sys
import re

def main(file):
    with open(file) as f:
        t = f.read()
    total = 0
    for term in re.finditer(r'mul\((\d{1,3}),(\d{1,3})\)', t):
        print(term.group(0))
        total += int(term.group(1)) * int(term.group(2))
    print(total)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main('input')
