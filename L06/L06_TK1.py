from random import randint
m = 0
n = 0
while m < 3 or n < 4:
    print("Minimum matrix size 3x4")
    m = int(input("Matrix width M: "))
    n = int(input("Matrix height N: "))
numbers = [[0] * n for i in range(m)]
for i in range(m):
    for j in range (n):
        numbers[i][j] = (randint(1, 100))
        print("%4d" %numbers[i][j], end="")
    print()

temp_1 = []
for j in range(n):
    temp_1.append(numbers[2][j]) # 3rd row
print("Min of 3rd row = %4d" %min(temp_1))

temp_1 = []
for i in range(m):
    temp_1.append(numbers[i][1]) # 2nd column
print("Max of 2nd column = %4d" %max(temp_1))

temp_1 = [] #replacing 2nd and 4th columns
for i in range(m):
    temp_1.append(numbers[i][1])
for i in range(m):
    numbers[i][1] = numbers[i][3]
for i in range(m):
    numbers[i][3] = temp_1[i]

print("Matrix with replaced 2nd and 4th columns:")
for i in range(m):
    for j in range (n):
        print("%4d" %numbers[i][j], end="")
    print()

print("Elements of main diagonal:") #main diagonal
for i in range(min(m, n)):
    print("%4d" % numbers[i][i], end="")
print()