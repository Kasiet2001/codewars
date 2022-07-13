def luck_check(string):
    if string.isdigit():
        left = [int(string[i]) for i in range(len(string)//2)]
        if len(string) % 2 == 0 and string.isdigit():
            right = [int(string[i]) for i in range(len(string)//2, len(string))]
        else:
            right = [int(string[i]) for i in range(len(string)//2 + 1, len(string))]
    return sum(left) == sum(right)
print(luck_check('8610L3938'))
