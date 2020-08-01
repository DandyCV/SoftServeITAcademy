#Задано символьний рядок. Розробити програму, яка будує і друкує в алфавітному порядку множину малих,
#множину великих латинських  літер, які містяться у заданому рядку, і множину цифр, яких немає у рядку.
from random import randint

random_string = ""
for symbol in range(50):
    random_string += (chr(randint(32, 126)))
print("Random string:", random_string)

small_letters = set()
for symbol in random_string:
    if 96 < ord(symbol) < 123:
        small_letters.add(symbol)
print("Small letters in string:", tuple(sorted(small_letters)))

big_letters = set()
for symbol in random_string:
    if 64 < ord(symbol) < 91:
        big_letters.add(symbol)
print("Big letters in string:", tuple(sorted(big_letters)))

digits = set()
all_digits = set([str(x) for x in range(10)])
for symbol in random_string:
    if 47 < ord(symbol) < 58:
        digits.add(symbol)
print("Digits which absent in string:", tuple(sorted(all_digits - digits)))