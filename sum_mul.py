def sum_mul(n, m):
    total = 0
    if n > 0 and m > 0:
        for i in range(n, m, n):
            total += i
    else:
        total = 'INVALID'
    return total
print(sum_mul(4, -7))