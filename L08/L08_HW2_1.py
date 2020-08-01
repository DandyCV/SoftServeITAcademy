# Задано n рядочків символів.  Розробити програму, яка визначає і друкує окремо приголосні та голосні малі літери
# латинського алфавіту, які є в кожному рядку.
from random import randint


def random_strings(n):
    for string in range(n):
        random_string = ""
        for symbol in range(20):
            random_string += (chr(randint(32, 126)))
        print("Random string №%d: %s" %(string + 1, random_string))
        small_letters = set()
        for item in random_string:
            if 96 < ord(item) < 123:
                small_letters.add(item)
        print("Small letters in string №%d:" % string, small_letters)


random_strings(4)