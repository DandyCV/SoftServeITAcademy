user_list = []
sum_list = []
for number in range(5):
    user_list.append(float(input("Enter number %d (float) for your list: " % (number+1))))
user_sum = sum(user_list)
user_prod = 1
for number in user_list:
    user_prod *= number
print("User list:", user_list)
print("User list sum:", user_sum)
print("User list product:", user_prod)