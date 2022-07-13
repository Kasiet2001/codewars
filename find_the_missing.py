def find_missing(sequence):
    d = (sequence[-1] - sequence[0]) // len(sequence)
    correct = [sequence[0]] + [item + d for item in sequence[:-1]]
    return list(set(correct) - set(sequence))[0]

print(find_missing([1, 3, 5, 9]))