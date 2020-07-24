from random import randint
random_list = []

for number in range(10):
    random_list.append(randint(-100, 100))
print("Random list 1:", random_list)

index_max = random_list.index(max(random_list))
index_min = random_list.index(min(random_list))

temp = random_list[index_min]
random_list[index_min] = random_list[index_max]
random_list[index_max] = temp

print("Random list 2:", random_list)
