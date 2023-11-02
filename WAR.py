import random

class Solidier:

    def __init__(self ,name='Noname', heath=100):
        self.name = name
        self.heath = heath

    def set_name(self, name):
        self.name - name

    def make_kick(self, enemy):
        enemy.heath -= random.randint(10, 20)
        if enemy.heath < 0:
            enemy.heath = 0
        self.heath += 10
        print(f'{self.name} ударил {enemy.name}')
        print(f'{enemy.name} = {enemy.heath}')

class Battle:

    def __init__(self, soldier1, soldier2):
        self.solder1 = soldier1
        self.solder2 = soldier2
        self.result = 'Все только начинается'

    def battle(self):
        while self.solder1.heath > 0 and self.solder2.heath > 0:
            n = random.randint(1, 2)
            if n == 1:
                self.solder1.make_kick(self.solder2)
            else:
                self.solder2.make_kick(self.solder1)
        if self.solder1.heath > self.solder2.heath:
            self.result = self.solder1.name + '   ***ПОБЕДИЛ***   '
        else:
            self.result = self.solder2.name + '   ***ПОБЕДИЛ***   '

    def who_win(self):
        print(self.result)

fierst = Solidier('fierst', 140)
second = Solidier('second')
b = Battle(fierst, second)
b.battle()
b.who_win()



