#Задано символьний рядок,. Розробити програму, яка знаходить групи цифр, записаних підряд, і вилучає із них всі
# початкові нулі, крім останнього, якщо за ним знаходиться крапка. Друкує модифікований масив по сорок символів у рядку.
from random import randint

random_string = "000.001jh000.550opk00023.000dfe70000.0001"
for symbol in range(160):
    random_string += (chr(randint(46, 64)))
random_string += "ip001k0101.k001"
print("Random string:", random_string)

edited_list = []
random_list = list(random_string)
prev_elem = " "
for i in random_string:
    if random_list[0] == "0" and prev_elem not in ".0123456789" and len(random_list) == 1:
        random_list.pop(0)
    elif random_list[0] == "0" and prev_elem not in ".0123456789" and random_list[1] != ".":
        random_list.pop(0)
    else:
        prev_elem = random_list.pop(0)
        edited_list.append(prev_elem)
edited_string = "".join(edited_list)

strings = len(edited_string) / 40
if strings % 1:
    strings += 1
strings = int(strings)

print("Edited string:")
for line in range(strings):
    print(edited_string[line * 40:(line + 1) * 40])