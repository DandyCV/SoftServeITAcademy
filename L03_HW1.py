'''№1 Визначити чи рік високосний'''
year = int(input("Enter year "))
if year < 0:
    print("The years B.C. are not allowed")
else:
    print(year, "іs" if year % 4 == 0 else "іsn't", "leap year of", year // 100 + 1, "century")

'''№2 Площа фігури на вибір (прямокутник, трикутник, круг)'''
user_figure = int(input("What figute area do you want to calculate? 1 - rectangle, 2 - triangle, 3 - circle "))
if user_figure == 1:
    figure_size1 = float(input("Enter the value of rectangle first side "))
    figure_size2 = float(input("Enter the value of rectangle second side "))
    figure_area = figure_size1 * figure_size2
    print("The rectangle area =", figure_area)
elif user_figure == 2:
    figure_size1 = float(input("Enter the value of triangle side "))
    figure_size2 = float(input("Enter the value of triangle height to the side "))
    figure_area = figure_size1 * figure_size2 / 2
    print("The triangle area =", figure_area)
elif user_figure == 3:
    figure_size1 = float(input("Enter the value of circle radius "))
    figure_area = figure_size1 ** 2 * 3.14
    print("The circle area =", figure_area)
else:
    print("Wrong choice")


'''№3 Опис числа'''
user_number = int(input("Enter integer number between -1000 and 1000 "))
number_description = "is "
#к-сть цифр
if user_number <= -1000 or user_number >= 1000:
    number_description += "many-digits, "
if user_number > -1000 and user_number <= -100 or user_number >= 100 and user_number < 1000:
    number_description += "three-digit, "
elif user_number > -100 and user_number <= -10 or user_number >= 10 and user_number < 100:
    number_description += "two-digt, "
elif user_number > -10 and user_number < 10:
    number_description += "one-digit, "
#додатнє/від'ємне
if user_number < 0:
    number_description += "negative, "
elif user_number > 0:
    number_description += "positive, "
else:
    number_description += "it's Zero"
#парне/непарне
if user_number % 2 and user_number // 1:
    number_description += "odd"
elif  not user_number % 2 and user_number // 1:
    number_description += "even"

print(user_number, number_description)


'''№4 Чи поміщається кругла сцена в квадратному залі'''
hall_area = float(input("Enter hall area "))
stage_radius = float(input("Enter stage radius "))
pass_width = float(input("Enter pass width "))
print("You can place the scene. Good luck." if hall_area**0.5 * 0.5 - stage_radius >= pass_width else
      "You can't place the scene! Try another size.")


'''№5 Розміняти суму купюрами 200, 100, 10, 1 грн'''
user_sum = int(input("Enter the sum "))
total_banknotes = "You need: "
if user_sum < 1:
    print("You don't have enough money. Try next time!")
else:
    banknotes_200 = user_sum // 200

    if banknotes_200:
        total_banknotes += "200 grn banknotes - " + str(banknotes_200) + "; "
        user_sum -= 200 * banknotes_200
    banknotes_100 = user_sum // 100

    if banknotes_100:
        total_banknotes += "100 grn banknotes - " + str(banknotes_100) + "; "
        user_sum -= 100 * banknotes_100
    banknotes_10 = user_sum // 10

    if banknotes_10:
        total_banknotes += "10 grn banknotes - " + str(banknotes_10) + "; "
        user_sum -= 10 * banknotes_10

    if user_sum:
        total_banknotes += "1 grn coins - " + str(user_sum) + "; "

print(total_banknotes)