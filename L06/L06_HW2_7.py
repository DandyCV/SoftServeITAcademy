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

sorted_matrix = [[0] * columns for i in range(rows)]
sorted_indexes = []

for item in sorted(matrix[0]):
    sorted_indexes.append(matrix[0].index(item))

for i in range(rows):
    for j in range(columns):
        sorted_matrix[i][j] = matrix[i][sorted_indexes[j]]

print("Matrix with sorted columns:")
for i in range(rows):
    for j in range(columns):
        print("%4d" % sorted_matrix[i][j], end="")
    print()