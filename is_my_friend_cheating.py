def remov_nb(n):
    result = []
    seq_sum = n*(n + 1) // 2
    for x in range(1, n + 1):
        y = (seq_sum - x) // (x + 1)
        if y <= n and x * y == (seq_sum - x - y):
            result.append((x, y))
    return result
print(remov_nb(26))