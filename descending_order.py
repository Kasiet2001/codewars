def descending_order(num):
    a_sorted = sorted(str(num))
    num = ''.join(a_sorted)
    return int(num[::-1])
print(descending_order(15))