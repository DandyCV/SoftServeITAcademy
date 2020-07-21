user_number = 1
positive_counter = 0
negative_counter = 0
while user_number != 0:
    user_number = int(input("Enter integer number: "))
    if user_number > 0:
        positive_counter += 1
    elif user_number < 0:
        negative_counter += 1
total_counter = positive_counter + negative_counter
print("Total numbers count = %d\nPositive numbers %.2f%%\nNegative numbers %.2f%%"
      % (total_counter, positive_counter * 100 / total_counter, negative_counter * 100 / total_counter))