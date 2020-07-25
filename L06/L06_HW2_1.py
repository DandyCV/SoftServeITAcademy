from random import randint
columns = 5
rows = 3
matrix = [[0] * columns for i in range(rows)]
for i in range(rows):
    for j in range(columns):
        matrix[i][j] = randint(-10, 10)
        print("%4d" % matrix[i][j], end="")
    print()
print("-" * 26)

#добавляємо стовпець з сумами рядків
for i in range(rows):
    row_sum = sum(matrix[i])
    matrix[i].append(row_sum)
columns += 1

#добавляємо рядок з сумами стовпців
column_sum = 0
sum_list = []
for j in range(columns):
    for i in range(rows):
        column_sum += matrix[i][j]
    sum_list.append(column_sum)
    column_sum = 0
matrix.append(sum_list)
rows += 1


for i in range(rows):
    for j in range(columns):
        print("%4d" % matrix[i][j], end="")
    print()