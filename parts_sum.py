def parts_sums(ls):
    sums = [sum(ls[i:len(ls)]) for i in range(len(ls))]
    sums.append(0)
    return sums
print(parts_sums([]))
