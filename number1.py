class Point:

    def __new__(cls, *args, **kwargs):
        print(f'Вызов функции __new__ для {str(cls)}')
        return super().__new__(cls)

    def __init__(self, x, y):
        print(f'Вызов функции __init__ для {str(self)}')
        self.x = x
        self.y = y

p = Point(1,5)