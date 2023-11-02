class DataBase:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, user, password, port):
        self.user = user
        self.password = password
        self.port = port

    def __del__(self):
        print('ddfdfdf')
        DataBase.__instance = None

    def connect(self):
        print(f'соеденение с БД с настройками: user = {self.user}, psw = {self.password}, port = {self.port}')

    def close(self):
        print('Соеденение разорвано')

    def read(self):
        print('Чтение данных')

    def write(self, data):
        print(f'Запись данных: {data}')

d1 = DataBase('user1', 'psw1', 3000)
d1.connect()
# d2 = DataBase('user2', 'psw2', 3000)
# d2.connect()
print(d1)
