from random import randint
positive_list = []
negative_list = []
print("Generated numbers:",end="")
for number in range(20):
    random_number = randint(-5, 5)
    if random_number < 0:
        negative_list.append(random_number)
    elif random_number > 0:
        positive_list.append(random_number)
    print("%3d" % random_number, end="")
print()
print("Positive list:", positive_list)
print("Negative list:", negative_list)