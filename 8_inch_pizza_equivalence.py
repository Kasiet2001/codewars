def how_many_pizzas(n):
    import math
    pizzas = (math.pi * pow(n / 2, 2)) // (math.pi * pow(8 / 2, 2))
    slices = ((math.pi * pow(n / 2, 2)) % (math.pi * pow(8 / 2, 2))) // 6
    return f'pizzas: {int(pizzas)}, slices: {int(slices)}'
print(how_many_pizzas(12))