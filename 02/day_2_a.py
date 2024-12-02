def main(file):
    differences = []
    with open(file) as f:
        for line in f.readlines():
            reports = line.split()
            z = []
            for a, b in zip(reports, reports[1:]):
                z.append(int(a) - int(b))
            differences.append(z)
    print(sum([safe(x) for x in differences]))

def safe(z):
    all_inc = all([x > 0 for x in z])
    all_dec = all([x < 0 for x in z])
    if not all_inc and not all_dec:
        return 0
    if all([abs(x) < 4 and abs(x) > 0 for x in z]):
        return 1
    return 0


if __name__ == "__main__":
    main('input')
