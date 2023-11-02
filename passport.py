class Passport:

    def __init__(self, first_name, last_name, date, num):
        self.first_name = first_name
        self.last_name = last_name
        self.date = date
        self.num = num

    def printInfo(self):
        print (f'''
Имя: {self.first_name},
Фамилия: {self.last_name},
Дата рождения: {self.date},
Номер паспорта: {self.num}''')

class ForeignPassport(Passport):

    def __init__(self, first_name, last_name, date, num, country, visa):
        super().__init__(first_name, last_name, date, num)
        self.country = country
        self.visa = visa

    def print_info(self):
        super().printInfo()
        print('Страна:', self.country)
        print('Виза:', self.visa)

def passportList(obj):
    return (obj.print_info())

p1 = Passport('Ivan', 'Ivanov', '09.09.2006', '8545 458754')
fp = ForeignPassport('Petr', 'Petrov', '04/30/2000', 'GTR2822424', 'Russia', 'Chaina')
pl = []
pl.append(p1)
pl.append(fp)
for passport in pl:
    passport.printInfo()