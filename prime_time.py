def prime(n):
    if n > 1:
        sieve = list(range(n + 1))
        sieve[1] = 0
        for i in sieve:
            if i > 1:
                for j in range(i + i, len(sieve), i):
                    sieve[j] = 0
        sieve1 = [x for x in sieve if x != 0]
        return sieve1
    return []
print(prime(0))