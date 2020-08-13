#В класі Name визначте:
#атрибути для first name та last name (fname та lname відповідно);
#атрибут fullname що повертає first і last names;
#атрибут initials який повертає ініціали (перші літери first та last name, розділених ‘.’ .
class Name():
    def __init__(self, fname, lname):
        self.first_name = fname
        self.last_name = lname
        self.full_name = fname + ' ' + lname
        self.initials = fname[0].upper() + '.' + lname[0].upper() + '.'

    def __repr__(self):
        return '%s has initials %s' %(self.full_name, self.initials)


print(Name('Serhii', 'Velychko'))