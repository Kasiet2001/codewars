def odd_count(n):
    return len([i for i in range(n) if i % 2 != 0])
print(odd_count(15))