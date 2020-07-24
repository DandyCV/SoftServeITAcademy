from random import randint
random_list = []
user_list = []
sum_list = []
for number in range(5):
    random_list.append(randint(-100, 100))
for number in range(5):
    user_list.append(int(input("Enter number %d (integer) for your list: " % (number+1))))
for i in range(5):
    sum_list.append(random_list[i] + user_list[i])
print("Random list:", random_list)
print("User list:", user_list)
print("Sum of R and U lists:",sum_list)