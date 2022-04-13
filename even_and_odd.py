def even_and_odd(n):
    num = str(n)
    even = str()
    odd = str()
    for i in range(len(num)):
        if int(num[i]) % 2 == 0:
            even += num[i]
        else:
            odd += num[i]
    if odd == '':
        odd += '0'
    if even == '':
        even += '0'
    return int(even), int(odd)
print(even_and_odd(153))