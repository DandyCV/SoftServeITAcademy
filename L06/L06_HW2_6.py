from random import randint
columns = 10
rows = 10

matrix = [[0] * columns for i in range(rows)]
print("Matrix %d x %d:" % (columns, rows))
for i in range(rows):
    for j in range(columns):
        matrix[i][j] = randint(-100, 100)
        print("%4d" % matrix[i][j], end="")
    print()
print("-" * 42)

print("Matrix with replaced diagonals:")
for i in range(rows):
    temp = matrix[i][i]
    matrix[i][i] = matrix[i][-1 - i]
    matrix[i][-1 - i] = temp
    for j in range(columns):
        print("%4d" % matrix[i][j], end="")
    print()