def persistence(n):
    steps = 0
    total = 1
    while len(str(n)) != 1:
        for i in str(n):
            total *= int(i)
        steps += 1
        n, total = total, 1
    return steps
print(persistence(999))