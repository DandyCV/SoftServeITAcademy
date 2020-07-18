#Task 7
msg = "Sergey Velychko"
print(msg)
hello = "Hello"
print(hello + msg)
hello += " "
print(hello + msg)
msg = msg[:6] + " Veniaminovich " + msg[7:]
print(msg)
s = "colorless"
s = s[0:4] + "u" + s[4:]
print(s)
dish = "dish-es"
dish = dish[:4]
run = "run-ning"
run = run[:3]
nation = "nation-ality"
nation = nation[:6]
do = "un-do"
do = do[3:]
heat = "pre-heat"
heat = heat[4:]
print(dish, run, nation, do, heat)
print("-" * 35)


#Афоризми Пайтона
aphorisms = """Beautiful is better than ugly
Explicit is better than implicit
Simple is better than complex
Complex is better than complicated
Readability counts"""
print(aphorisms.upper())
print(aphorisms.lower())


#добуток цифр числа, реверс
user_number = input("Enter integer number from 0 to 9999\n")
if int(user_number) >= 0 and int(user_number) <= 9999:
    digits_sum = int(user_number[0]) + int(user_number[1]) + int(user_number[2]) + int(user_number[3])
    print("Sum of number digits =", digits_sum)
    print("Revers number is", user_number[-1::-1])
else:
    print("Wrong number")