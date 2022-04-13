def minimum_steps(numbers, value):
    summ = min(numbers)
    total = 0
    while summ < value:
        numbers.remove(min(numbers))
        summ += min(numbers)
        total += 1
    return total
print(minimum_steps([8,9,10,4,2], 23))
