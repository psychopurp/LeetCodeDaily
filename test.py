
data = [[1, 1, 0], [1, 1, 1], [1, 1, 1]]


def setZeroes(matrix):
    """
    Do not return anything, modify matrix in-place instead.
    """
    col, row = False, False
    if matrix[0][0] == 0:
        col, row = True, True
    for i in range(len(matrix)):
        if matrix[i][0] == 0:
            col = True
        for j in range(len(matrix[i])):

            if i == 0 and matrix[i][j] == 0:
                row = True
            if matrix[i][j] == 0:
                matrix[0][j] = 0
                matrix[i][0] = 0

    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[i])):
            if matrix[0][j] == 0 or matrix[i][0] == 0:
                matrix[i][j] = 0
        if col:
            matrix[i][0] = 0

    if row:
        for j in range(len(matrix[0])):
            matrix[0][j] = 0


setZeroes(data)
print(data)
