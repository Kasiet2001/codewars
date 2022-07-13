def sum_two_smallest_numbers(numbers):
    sorted_numbers = sorted(numbers)
    return sorted_numbers[0] + sorted_numbers[1]
print(sum_two_smallest_numbers([5, 8, 12, 18, 22]))