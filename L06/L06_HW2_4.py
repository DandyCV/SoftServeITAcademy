from random import randint
columns = 5
rows = 4

matrix = [[0] * columns for i in range(rows)]

for i in range(rows):
    for j in range(columns):
        matrix[i][j] = randint(-100, 100)
        print("%4d" % matrix[i][j], end="")
    print()
print("-" * 26)

min_elements = []

for j in range(columns):
    column_elements = []
    for i in range(rows):
        column_elements.append(matrix[i][j])
    min_elements.append(min(column_elements))

print("Max element of minimal column elements = %d" % max(min_elements))