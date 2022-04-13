def calc(x):
    total1 = str()
    a = 0
    b = 0
    for i in range(len(x)):
        total1 = total1 + str(ord(x[i]))
    total2 = total1.replace('7', '1')
    for j in range(len(total1)):
        a += int(total1[j])
    for k in range(len(total2)):
        b += int(total2[k])
    return a - b
print(calc('ifkhchlhfd'))