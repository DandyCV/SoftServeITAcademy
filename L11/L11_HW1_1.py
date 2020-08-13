#В класі Person визначте метод compare_age(), який повертатиме результат порівняння віку людини з Вашим віком.
# При заданих об’єктах p1, p2 і p3, які будуть ініціалізовані name та age,
#буде повертатися повідомлення наступного формату:
#{other_person} is {older than / younger than / the same age as} me.
class Person():

    def __init__(self, p1, p2, p3):
        self.your_name = p1
        self.your_age = p2
        self.my_age = p3

    def compare_age(self):
        message = ''
        if self.your_age > self.my_age:
            message = 'older than'
        elif self.your_age < self.my_age:
            message = 'younger than'
        else:
            message = 'the same age as'
        print('%s is %s me.' %(self.your_name, message))


p = Person('Dan', 27, 31)
p.compare_age()