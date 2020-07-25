columns = 40
rows = 25
matrix = [[0] * columns for i in range(rows)]
numbers = list(range(1000))

numbers_2d = 0
for i in range(rows):
    for j in range(columns):
        matrix[i][j] = numbers.pop(0)
        if 9 < matrix[i][j] < 100:
            numbers_2d += 1
        print("%4d" % matrix[i][j], end="")
    print()
print("-" * 161)

print("Matrix contains %d 2-digit numbers" % numbers_2d)
