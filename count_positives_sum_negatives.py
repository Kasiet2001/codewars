def count_positives_sum_negatives(arr):
    count_positives = 0
    sum_negatives = []
    if len(arr) == 0:
        return []
    for i in range(len(arr)):
        if arr[i] > 0:
            count_positives += 1
        else:
            sum_negatives.append(arr[i])
    return [count_positives, sum(sum_negatives)]
print(count_positives_sum_negatives([]))