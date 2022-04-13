def divisors(integer):
    divisors = []
    for i in range(2, integer):
        if integer % i == 0:
            divisors.append(i)
    if len(divisors) == 0:
        divisors = f'{integer} is prime'
    return divisors
print(divisors(3))