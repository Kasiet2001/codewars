def get_real_floor(n):
    if 0 < n < 13:
        return n - 1
    elif n >= 13:
        return n - 2
    else:
        return n
print(get_real_floor(15))