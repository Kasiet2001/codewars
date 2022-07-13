def move_zeros(lst):
    b = lst.count(0)
    a = lst.copy()
    while len(a) - len(lst) != b:
        for i in lst:
            if i == 0:
                lst.remove(0)
    return lst + ([0] * b)
print(move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]))