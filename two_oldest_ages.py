def two_oldest_ages(ages):
    oldest_ages = sorted(ages)
    return [oldest_ages[-2], oldest_ages[-1]]
print(two_oldest_ages([6, 5, 83, 5, 3, 18]))