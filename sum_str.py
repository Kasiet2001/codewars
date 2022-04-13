def sum_str(a, b):
    return str(int(a) + int(b)) if a.isdigit() and b.isdigit() else a or b or 0
print(sum_str('', ''))