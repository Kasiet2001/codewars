def comp(array1, array2):
    '''total = 0
    if array1 == [] or array2 == []:
        return False
    elif type(array1) != list or type(array2) != list:
        return False
    else:
        for i in array2:
            if i ** 0.5 in array1:
                total += 1
    return total == len(array1)
print(comp([121, 144, 19, 161, 19, 144, 19, 11], [121, 14641, 20736, 361, 25921, 361, 20736, 361]))'''
    from collections import Counter
    return True if (lambda a, b: a != None and b != None) and Counter(map(lambda x: x * x, array1)) == Counter(array2) else False
print(comp([121, 144, 19, 161, 19, 144, 19, 11], [121, 14641, 20736, 361, 25921, 361, 20736, 361]))


