P = 3
H = 7
user_number = 0
numbers_sum = 0
numbers_product = 1
in_range_counter =0

while user_number != P and user_number != H:
    user_number = int(input("Enter the number: "))
    if user_number < P:
        numbers_sum += user_number
    elif user_number > H:
        numbers_product *= user_number
    else:
        in_range_counter += 1

print("Sum of numbers < %d = %d\nProduct of numbers > %d = %d\n\
Quantity of number in range from %d to %d = %d"
      %(P, numbers_sum, H, numbers_product, P, H, in_range_counter))
