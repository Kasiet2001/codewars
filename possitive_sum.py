def positive_sum(arr):
    return sum(arr[i] for i in range(len(arr)) if arr[i] > 0)
print(positive_sum([0, -2, 0, 5]))