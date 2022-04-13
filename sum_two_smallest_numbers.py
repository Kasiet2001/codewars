def sum_two_smallest_numbers(numbers):
    a = min(numbers)
    numbers.remove(a)
    b = min(numbers)
    return a + b
print(sum_two_smallest_numbers([7, 15, 12, 18, 22]))