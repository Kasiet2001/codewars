def modified_sum(a, n):
    return sum(i ** n - i for i in a)
print(modified_sum([1, 2, 3], 3))