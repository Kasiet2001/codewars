def find_uniq(arr):
    set_arr = set(arr)
    return [i for i in set_arr if arr.count(i) == 1][0]
print(find_uniq([ 0, 0, 0.55, 0, 0 ]))