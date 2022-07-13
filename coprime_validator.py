def are_coprime(n,m):
    a = []
    for i in range(1, min(n, m) + 1):
        if n % i == 0 and m % i == 0:
            a.append(i)
    if len(a) > 1:
        return False
    return True
print(are_coprime(20, 27))