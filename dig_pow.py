def dig_pow(n, p):
    a = []
    a.extend(str(n))
    total = sum(int(a[i]) ** (p + i) for i in range(len(a)))
    return -1 if total % n != 0 else total // n
print(dig_pow(92, 1))