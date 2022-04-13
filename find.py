def find(a,b,n):
    result = f'{a}{b}'
    if int(result) == 0:
        return 0
    else:
        while len(result) <= n:
            result += str(int(result[-1]) + int(result[-2]))
        return result[n]
print(find(0,0,1000000))