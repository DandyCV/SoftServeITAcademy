from random import randint
random_list = []

for number in range(20):
    random_list.append(randint(-10, 10))

print("Random list:", random_list)
random_list = [x for x in random_list if x >= 0]
print("Radom list withot negative numbers:", random_list)

index_list = [x for x in range(len(random_list)) if random_list[x] % 2 == 0]
print("List with indexes of even numbers:", index_list)

print("Unique elements:", end="")
for item in random_list:
    if random_list.count(item) == 1:
        print("%2d" % item, end="")
print()
