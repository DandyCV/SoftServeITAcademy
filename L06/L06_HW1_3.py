from random import randint
random_list = []
for number in range(20):
    random_list.append(randint(-5, 4))
positive_counter = 0
negative_counter = 0
zero_counter = 0
for number in random_list:
    if number == 0:
        zero_counter += 1
    elif number < 0:
        negative_counter += 1
    else:
        positive_counter += 1

print("Random list:", random_list)
print("Positive count:", positive_counter)
print("Negative count:", negative_counter)
print("Zero count:", zero_counter)