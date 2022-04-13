def vaporcode(s):
    a = []
    for i in range(len(s)):
        if s[i] != ' ':
            a.append(s[i].upper())
    return '  '.join(a)
print(vaporcode('Lets go to the movies'))