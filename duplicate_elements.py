def duplicate_elements(m, n):
    total = 0
    for i in range(len(m)):
        if m[i] in n:
            total += 1
    return True if total > 0 else False
print(duplicate_elements([9, 8, 7], [8, 1, 3]))