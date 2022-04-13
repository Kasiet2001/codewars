def solve(arr):
    maxx = max(arr)
    arr.remove(maxx)
    if maxx > sum(arr):
        return sum(arr)
    else:
        return (maxx + sum(arr)) // 2
print(solve([8,2,8]))