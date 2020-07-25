columns = 5
rows = 4
matrix = [[0] * columns for i in range(rows)]

for i in range(rows):
    for j in range(columns - 1):
        matrix[i][j] = int(input("Enter matrix element of %d column, %d row: " % (i + 1, j + 1)))
    matrix[i][columns - 1] = sum(matrix[i])

for i in range(rows):
    for j in range(columns):
        print("%4d" %matrix[i][j], end="")
    print()