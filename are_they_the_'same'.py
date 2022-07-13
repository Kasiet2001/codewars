def comp(array1, array2):
    a = 0
    if array1 == None or array2 == None:
        return False
    elif len(array1) == len(array2):
        for i in range(len(array1)):
            for j in range(len(array2)):
                if array1[i] ** 2 == array2[j]:
                    a += 1
                    del array2[j]
                    break
        return a == len(array1)
    return False
print(comp(None, None))