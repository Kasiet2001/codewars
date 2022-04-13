def find_difference(a, b):
    list1 = 1
    list2 = 1
    for i in a:
        list1 *= i
    for j in b:
        list2 *= j
    return abs(list1 - list2)
print(find_difference([3, 2, 5], [1, 4, 4]))
