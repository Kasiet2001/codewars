def gimme(input_array):
    for i in input_array:
        if min(input_array) < i < max(input_array):
            return input_array.index(i)
print(gimme([2, 3, 1]))