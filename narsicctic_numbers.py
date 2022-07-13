def is_narcissistic(i):
    sum_of_cubes = sum(int(x)**len(str(i)) for x in str(i))
    return sum_of_cubes == i
print(is_narcissistic(201))