#Задано символьний рядок. Розробити програму, яка вилучає з цього рядка всі повторні входження цифр
# і знаків арифметичних операцій.
from random import randint

random_string = ""
for symbol in range(50):
    random_string += (chr(randint(41, 65)))
print("Random string: %s" % random_string)


for symbol in "0123456789+-/*><=":
    index = random_string.find(symbol)
    if index > 0:
        str_slice = random_string[index + 1:].replace(symbol, "")
        random_string = random_string[:index + 1] + str_slice

print("Edited string: %s" % random_string)