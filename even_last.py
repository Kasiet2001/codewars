def even_last(numbers):
    total = 0
    if len(numbers) > 0:
        for i in range(len(numbers)):
            if i % 2 == 0:
                total = total + numbers[i]
        return total * numbers[-1]
    else:
        return 0
print(even_last([]))