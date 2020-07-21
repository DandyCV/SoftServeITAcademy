user_number = 1
positive_counter = 0
total_counter = 0
while user_number != 0:
    user_number = int(input("Enter integer number: "))
    if user_number > 0:
        positive_counter += 1
    total_counter += 1
print("Total quantity of numbers = %d\nPositive numbers %.2f\n \
Negative numbers %.2f" %(total_counter, positive_counter * 100 /))