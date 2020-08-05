# Створіть словник, ключами є слова, а значеннями – список слів-синонімів до нього. Програма отримує на вхід кількість слів N. Далі користувач вводить слова-ключі та відповідні йому синоніми.
#Передбачити:
#1) на запит (слово) користувача вивести список синонімів;
#2) користувач вводить речення, в якому є слова (ключі, що містяться в словнику). Замінити їх синонімами та вивести речення на екран.

from random import randint

synonims = {"beautiful": ["pretty", "charming"],
            "warm": ["hot", "friendly"],
            "kind": ["good", "well"],
            "magic": ["fairy", "imaginary"],
            "nice": ["pleasant", "fine"],
            "modest": ["discreet"]}

word = input("Input a word please: ")

if word in synonims.keys():
    print("For %s has %d synonims: " % (word, len(synonims[word])))
    print(synonims[word])
else:
    print("There is not such a word in dictionary.")

sent = input("Input a sentence please: ")

for key in synonims:
    if sent.find(key) >= 0:
        syn_list = synonims[key]
        sent = sent.replace(key, syn_list[randint(0, len(synonims[key]) - 1)])

print(sent)
