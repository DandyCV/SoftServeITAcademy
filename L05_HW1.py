#вгадай номер
from random import randint
number = randint(1, 100)
counter = 1
print("Try to guess my number from 1 to 100")
while counter <= 10:
    user_number = int(input("It's your %d/10 attempt: " % counter))
    counter += 1
    if number == user_number:
        print("You WIN!")
        break
    elif number < user_number:
        print("My number is lower")
    else:
        print("My number is bigger")
else:
    print("You LOSE!")
