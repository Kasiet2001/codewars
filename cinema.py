def cinema(b, g):
    print(b, g)
    order = str()
    if b == g:
        order += 'BG' * g
    elif max(b, g) == b and b - g == 1:
        order += 'B'
        while len(order) != b + g:
            order += 'GB'
    elif max(b, g) == g and g - b == 1 :
        order += 'G'
        while len(order) != b + g:
            order += 'BG'
    return order
print(cinema(1, 5))
