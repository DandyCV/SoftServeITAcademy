columns = 4
rows = 3
matrix_1 = [[0] * columns for i in range(rows)]
matrix_2 = [[0] * columns for j in range(rows)]
max_matrix = [[0] * columns for k in range(rows)]

for i in range(rows):
    for j in range(columns):
        matrix_1[i][j] = int(input("Enter matrix №1 element of %d column, %d row: " % (i + 1, j + 1)))

for i in range(rows):
    for j in range(columns):
        matrix_2[i][j] = int(input("Enter matrix №2 element of %d column, %d row: " % (i + 1, j + 1)))
        max_matrix[i][j] = max(matrix_1[i][j], matrix_2[i][j])

print("Matrix №1:")
for i in range(rows):
    for j in range(columns):
        print("%4d" % matrix_1[i][j], end="")
    print()

print("Matrix №2:")
for i in range(rows):
    for j in range(columns):
        print("%4d" % matrix_2[i][j], end="")
    print()

print("Matrix with MAX elements:")
for i in range(rows):
    for j in range(columns):
        print("%4d" % max_matrix[i][j], end="")
    print()
