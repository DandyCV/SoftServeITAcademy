#числа кратні 5
number_counter = 1
multiple5_counter = 0
print("Enter 10 integer numbers bigger than 2")
while number_counter <= 10:
    number = int(input("Enter number %d: " % number_counter))
    while number <= 2:
        number = int(input("Number should be greater than 2: "))
    if not number % 5:
        multiple5_counter += 1
    number_counter += 1
print("There was %d number(s) multiple of five." % multiple5_counter)
