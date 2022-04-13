def square_sum(numbers):
    return sum((numbers[i])**2 for i in range(len(numbers)))
print(square_sum([0, 3, 4, 5]))