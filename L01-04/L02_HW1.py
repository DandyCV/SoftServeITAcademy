'''Задана вага в грамах, визначити вагу в тона і кілограмах'''
weight_in_grams = float(input("Enter weight in grams: "))
print("Weight in kilograms =", weight_in_grams / 10**3, "\nWeight in tons =", weight_in_grams / 10**6)


'''Відомий обсяг інформації в байтах. Перевести в кілобайти, мегабайти'''
information_in_bytes = int(input("Enter quantity of information in bytes: "))
print("Quantity of information in kilobytes =", information_in_bytes / 2**10,
      "\nQuantity of information in megabytes =", information_in_bytes / 2**20)

'''Поміняти місцями значення змінних'''
user_var_1 = input("Enter the value of first variable: ")
user_var_2 = input("Enter the value of second variable: ")
user_var_1, user_var_2 = user_var_2, user_var_1
print(user_var_1, user_var_2)


'''Площа і периметр прямокутника'''
rectangle_width = float((input("Enter value of rectangle width: ")))
rectangle_height = float((input("Enter value of rectangle height: ")))
print("The acreage of rectangle =", rectangle_height * rectangle_width,
      "\nThe perimeter of rectagle =", rectangle_width * 2 + rectangle_height * 2)

'''Площа і довжина кола'''
circle_radius = float((input("Enter value of circle_radius: ")))
print("The acreage of circle =", circle_radius**2 * 3.14,
      "\nThe lenght of circle =", circle_radius * 2 * 3.14)


'''Визначення гіпотенузи за 2-ма катетами'''
triangle_cathetus_1 = float((input("Enter value of first cathetus: ")))
triangle_cathetus_2 = float((input("Enter value of second cathetus: ")))
print("The triangle hypotenuse =", (triangle_cathetus_1**2 + triangle_cathetus_2**2)**(1/2))