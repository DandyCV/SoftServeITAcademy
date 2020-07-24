from random import randint
random_list = []

for number in range(10):
    random_list.append(randint(-100, 100))
print("Random list 1:", random_list)

'''Я помітив що, якщо мінімальний елемент знаходиться лівіше максимального то заміна не відбувається, оскільки
в момент пошуку куди запихнути найменьший елемент з temp'у, заново обчислюється індекс найбільшого. 
А в цей момент ми маємо в списку 2 однакових найбільших елементи і відповідно повертається індекс лівішого з них. 
А за цим індексом до цього був найменший елемент. І тоді ми найменший елемент з temp'у засовуємо в той самий індекс
(тобіто нічого не змінюється). Для цього я перевіряю який елемент лівіше, найбільший чи найменший і відповідно в temp
присвоюю той, що правіше. Таск з лекції також працює наполовину =)'''
if random_list.index(min(random_list)) > random_list.index(max(random_list)):
    temp = random_list[random_list.index(min(random_list))]
    random_list[random_list.index(min(random_list))] = random_list[random_list.index(max(random_list))]
    random_list[random_list.index(max(random_list))] = temp
else:
    temp = random_list[random_list.index(max(random_list))]
    random_list[random_list.index(max(random_list))] = random_list[random_list.index(min(random_list))]
    random_list[random_list.index(min(random_list))] = temp
print("Random list 2:", random_list)
