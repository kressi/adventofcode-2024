def main(file):
    a = []
    b = []
    diff = 0
    with open(file) as f:
        for line in f.readlines():
            x = line.split()
            a.append(int(x[0]))
            b.append(int(x[1]))
    a.sort()
    b.sort()
    for x, y in zip(a, b):
        diff += abs(x - y)
    print(diff)

if __name__ == "__main__":
    main('input')
