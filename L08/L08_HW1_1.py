from random import randint
random_list = []
for symbol in range(30):
    random_list.append(chr(randint(32,126)))

print("Random list:", random_list)

letter_list = []
digit_list = []
symbol_list = []
for item in random_list:
    if 47 < ord(item) < 58:
        digit_list.append(item)
    elif 64 < ord(item) < 91 or 96 < ord(item) < 123:
        letter_list.append(item)
    else:
        symbol_list.append(item)

letter_tuple = tuple(letter_list)
digit_tuple = tuple(digit_list)
symbol_tuple = tuple(symbol_list)
print("Only letters:", letter_tuple)
print("Only digit:", digit_tuple)
print("Only symbols:", symbol_tuple)

user_symb = input("Enter a letter: ")
print("Letter has index: %d" % letter_tuple.index(user_symb))
user_symb = input("Enter a digit: ")
print("Digit has index: %d" % digit_tuple.index(user_symb))
user_symb = input("Enter a symbol: ")
print("Symbol has index: %d" % symbol_tuple.index(user_symb))

print("Letters in back order:", tuple(reversed(letter_tuple)))
