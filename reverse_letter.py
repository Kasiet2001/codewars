def reverse_letter(string):
    s = str()
    for i in range(len(string)):
        if 96 < ord(string[i]) < 123:
            s += string[i]
    return s[::-1]
print(reverse_letter("ultr53o?n"))