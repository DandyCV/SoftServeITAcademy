#У змінній записаний текст. Словом вважається послідовність непорожніх символів, які йдуть підряд,
#слова розділені одним або більше пробілом.
#Програмно створіть словник, в якому ключами є слова з речення, а значеннями – кількість входження в речення.

user_text = "Often, you want to use a default value if a key is not present." \
            " For example, if there is no salary for Mike, you want to get an average salary instead."\
            " Instead of using the in operator, you can simply call the get() method " \
            "and pass the key and a default value." \
            " The default value is returned if there is no matching key."

print(user_text)

user_text = user_text.lower()
edited_text = ""

for i in range(len(user_text)):
    if 96 < ord(user_text[i]) < 123 or ord(user_text[i]) == 32:
        edited_text += user_text[i]

text_list = edited_text.split(" ")
text_dict = {}

for word in text_list:
    if word in text_dict:
        text_dict[word] += 1
    else:
        text_dict[word] = 1

for word in text_dict:
    print('"%s": %d' %(word.capitalize(), text_dict[word]))
