#Задано два символьних рядка із малих і великих латинських літер та цифр.
# Розробити програму, яка будує і друкує в алфавітному порядку множину літер, які є в обох масивах,
# і множини літер окремо першого і другого масивів.
from random import randint


def random_string(length):
    rand_str = ""
    for num in range(length):
        cod = randint(48, 122)
        if 47 < cod < 58 or 64 < cod < 91 or 96 < cod < 123:
            rand_str += (chr(cod))
    return rand_str


random_string1 = random_string(30)
random_string2 = random_string(30)
print("Random string №1:", random_string1)
print("Random string №2:", random_string2)


def sets_letters_intersection(str1, str2):
    numbers = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
    set1 = set(str1) - numbers
    set2 = set(str2) - numbers
    in_set = set1.intersection(set2)
    return set1, set2, in_set


int_sets = sets_letters_intersection(random_string1, random_string2)
str1_set = sorted(int_sets[0])
str2_set = sorted(int_sets[1])
inter_set = sorted(int_sets[2])
print("String №1 letters:", str1_set)
print("String №2 letters:", str2_set)
print("String #1 and String №2 letters:", inter_set)
