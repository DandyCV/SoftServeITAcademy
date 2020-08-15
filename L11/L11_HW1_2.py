#Визначте атрибути fullname та email в класі Employee. При заданих first та last names:
#- В конструкторі сформуйте fullname звичайним з’єднанням через пробіл first та last name.
#В конструкторі сформуйте email з’єднанням first та last name через ‘.’ між ними та приєднуючи
# ‘@company.com’ наприкінці.
class Employee():
    def __init__(self, first, last):
        self.first_name = first
        self.last_name = last
        self.full_name = first + ' ' + last
        self.email = first.lower() + '.' + last.lower() + '@company.com'

    def __repr__(self):
        return '%s your email address: %s' %(self.full_name, self.email)


print(Employee('Serhii', 'Velychko'))