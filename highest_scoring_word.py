def high(x):
    total = 0
    b = []
    x = x.split()
    for i in x:
        for j in i:
            total += ord(j) - 96
        b.append(total)
        total = 0
    return x[b.index(max(b))]
print(high('man i need a taxi up to ubud'))