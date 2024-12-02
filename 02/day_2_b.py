def main(file):
    all_reports = []
    with open(file) as f:
        for line in f.readlines():
            z = [int(x) for x in line.split()]
            all_reports.append(z)
    print(sum([1 if safe_any(x, -1) else 0 for x in all_reports]))

def safe_any(z0, off):
    if off >= len(z0):
        return 0
    if off < 0:
        z1 = z0
    else:
        z1 = [x for i, x in enumerate(z0) if i != off]
    z = []
    for a, b in zip(z1, z1[1:]):
        z.append(int(a) - int(b))
    is_safe = safe(z)
    if is_safe > 0:
        return is_safe
    return safe_any(z0, off + 1)

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
