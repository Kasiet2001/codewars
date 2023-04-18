def multiplication_table(size):
    table = []
    for i in range(1, size + 1):
        table.append([j * i for j in range(1, size + 1)])
    return table


def multiplication_table(size):
    return [[j * i for j in range(1, size + 1)] for i in range(1, size + 1)]
print(multiplication_table(3))



