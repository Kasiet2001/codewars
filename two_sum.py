def two_sum(numbers, target):
    a = numbers.copy()
    for i in numbers:
        a[a.index(i)] = 0
        for j in a:
            if i + j == target:
                first_index = numbers.index(i)
                second_index = a.index(j)
    return [first_index, second_index]
print(two_sum([2,2,3], 4))