# def positive_sum(arr):
#     total = 0
#     for i in range(len(arr)):
#         if arr[i] > 0:
#             total += arr[i]
#     return total


def positive_sum(arr):
    return sum(arr[i] for i in range(len(arr)) if arr[i] > 0)
print(positive_sum([0, -2, 0, 5]))