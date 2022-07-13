def alternate(n, first_value, second_value):
    s = []
    while len(s) < n:
        s.append(first_value)
        if len(s) >= n:
            break
        else:
            s.append(second_value)
    return s
print(alternate(5, "lemons", "apples"))

def alternate(n, first_value, second_value):
    return [first_value if x % 2 == 0 else second_value for x in range(n)]
print(alternate(5, "lemons", "apples"))