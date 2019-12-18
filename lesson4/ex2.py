import datetime

d = [{'login': 'admin', 'password': 'admin', 'users': None}, ]

class Reg:
    
    def __init__(self, login, password):
        self._login = login
        self._password = password
    def add_(x):
        x.append({'login': self._login, 'password': self._password})


class Autor(Reg):
    def __init__(self, login, password):
        super().__init__(login, password)


class Admin:
    pass


class User:
    pass


user = []
d = [{'login': 'admin', 'password': 'admin', 'users': user}, ]
while True:

    try:
        sing = int(input('хотите войти (1) или зарегистрироваться (0)'))
    except:
        sing = 0

    if sing == 1:
        login = input('Введите логин:')
        password = input('Введите пароль:')
        if login == 'admin' and password == 'admin' :
            print('-'*80)
            print('вы вошли как администротор')
            print(d[1:][:])
            break
        elif login != 'admin' and password != 'admin' :
            for i in d:
                try:
                    if i['login'] == login and i['password'] == password:
                        print(i)
                        break
                except:
                    print('error')
        else:
            f = input('неверный логин или пароль, хотите попробывать еще раз ?')
            if f == 1:
                break
    elif sing == 0:
        login = input('Введите логин для регистрации:')
        password = input('Введите пароль для регистрации:')
        new = {'login': login,
               'password': password,
               'date': (datetime.datetime.now().hour, datetime.datetime.now().minute, datetime.datetime.now().year)}
        d.append(new)


new_post = str(input())
