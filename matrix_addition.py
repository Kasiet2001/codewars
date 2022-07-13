def matrix_addition(a, b):
    for i in range(len(a)):
        for j in range(len(a[i])):
            a[i][j] += b[i][j]
    return a
print(matrix_addition([ [1, 2, 3],
    [3, 2, 1],
    [1, 1, 1] ],
#       +
  [ [2, 2, 1],
    [3, 2, 3],
    [1, 1, 3] ] ))