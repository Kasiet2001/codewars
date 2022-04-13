def count_sheep(n):
    sheep = str()
    for i in range(n):
        sheep += str(i + 1) + ' sheep...'
    return sheep
print(count_sheep(0))
