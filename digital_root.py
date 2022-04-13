def digital_root(n):
    a = []
    while len(str(n)) > 1:
        a.extend(str(n))
        n = sum(int(i) for i in str(n))
    return n
print(digital_root(132189))