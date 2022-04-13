def calculator(txt):
    txt = txt.split()
    if '-' in txt and (len(txt[0]) - len(txt[2])) > 0:
        return (len(txt[0]) - len(txt[2])) * '.'
    elif '-' in txt and (len(txt[0]) - len(txt[2])) == 0:
        return ''
    elif '+' in txt:
        return (len(txt[0]) + len(txt[2])) * '.'
    elif '*' in txt:
        return (len(txt[0]) * len(txt[2])) * '.'
    else:
        return (len(txt[0]) // len(txt[2])) * '.'
print(calculator(". - ."))