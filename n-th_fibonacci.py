def nth_fib(n):
    fib = [0, 1]
    for i in range(2, n + 1):
        next_num = fib[-1] + fib[-2]
        fib.append(next_num)
    return fib[n - 1]
print(nth_fib(7))