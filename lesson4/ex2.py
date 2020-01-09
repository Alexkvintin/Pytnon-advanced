import datetime
d = [{'login': 'admin', 'password': 'admin'}, ]
g=0

class Reg:

    def __init__(self, login, password):
        self._login = login
        self._password = password

    def _add(self):
        f = 0
        for i in d:
            if i['login'] == self._login:
                print('Такой пользователь уже зарегистрирован ! ')
            else:
                f += 1
                pass
            if len(self._password) >= 8 and any([x.isdigit() for x in self._password]) == True and any(
                    [x.isupper() for x in self._password]) == True:
                f += 1
            else:
                print('слишком простой пароль ! ')
            if f == 2:
                d.append({'login': str(login), 'password': str(password),
                          'date': (
                              datetime.datetime.now().day, datetime.datetime.now().month, datetime.datetime.now().year),
                          'posts': None})
                print('Регистрация успешна ! ')
                return d


class Admin(Reg):
    def admin(self):
        print('-' * 35)
        print('Добро пожаловать', login, '\n', d, '\n', '-' * 35)


class Autor(Reg):
    def __init__(self, login, password):
        super().__init__(login, password)
        if self._login == 'admin' and self._password == 'admin':
            Admin.admin(self)
        else:
            User.search(self)


class User(Autor):
    def search(self):
        u = 0
        for i in d:
            if i['login'] == login and i['password'] == password:
                print('-' * 35)
                print('Добро пожаловать', login, '\n', i, '\n', '-' * 35)
                u += 1
                break
            elif u != 1 and i['login'] != 'admin' and i['password'] == 'admin':
                print('не верно введенные логин или пароль!')

    def new_post(x):
        for i in d:
            if i['login'] == login and i['password'] == password:
                t = (datetime.datetime.now().day, datetime.datetime.now().month, datetime.datetime.now().year)
                if i['posts'] is None:
                    b = [t, x]
                    i['posts'] = b
                    break
                else:
                    g = [t, x]
                    i['posts'].append(g)


while True:
    try:
        sing = int(input('хотите войти (1) или зарегистрироваться (0)'))
    except:
        sing = 0

    if sing == 1:
        login = input('введите логин')
        password = input('введите пароль')
        sin = Autor(login, password)
        if login != 'admin' and password != 'admin':
            x = input('хотите написать пост? (1-да enter-нет)')
            if x == '1':
                while True:
                    _time = (datetime.datetime.now().day, datetime.datetime.now().month, datetime.datetime.now().year)
                    data = input('напишите пост')
                    user = User.new_post(data)
                    y = input('хотите написать еще пост, или выйти ? (1-написать пост enter-выход)')
                    if y == '1':
                        continue
                    else:
                        break
            else:
                pass
    elif sing == 0:
        login = input('введите логин: ')
        password = input('введите пароль: ')
        password_2 = input('повторите пароль: ')
        if password_2 != password:
            print('пароли не совпадают ! \n повторите регистрацию !')
        else:
            New = Reg(login, password)
            New._add()
