def largest_pair_sum(numbers):
    numbers.sort()
    return numbers[-1] + numbers[-2]
print(largest_pair_sum([-100,-29,-24,-19,19]))