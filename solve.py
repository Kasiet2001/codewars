def solve(nums, div):
    return [i + i % div for i in nums]
print(solve([1000, 999, 998, 997], 5))