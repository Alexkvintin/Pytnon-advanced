import datetime

d = [{'login' : 'admin', 'password' : 'admin'}, ]


class Reg :

    def __init__(self, login, password) :
        self._login = login
        self._password = password

    def _add(self) :
        d.append({'login' : str(login), 'password' : str(password),
                  'date' : (datetime.datetime.now().day, datetime.datetime.now().month, datetime.datetime.now().year),
                  'posts' : None})
        return d


class Admin(Reg) :
    def admin(self) :
        print('Добро пожаловать', login)
        print(d)


class Autor(Reg) :
    def __init__(self, login, password) :
        super().__init__(login, password)
        if self._login == 'admin' and self._password == 'admin' :
            Admin.admin(self)
        else :
            User.search(self)


class User(Autor) :
    def search(self) :
        for i in d :
            try :
                if i['login'] == login and i['password'] == password :
                    print('Добро пожаловать', login, '\n',
                          i)
                    break
            except :
                print('пользователь не верно введенные логин или пароль!')

    def new_post(x) :
        for i in d :
            if i['login'] == login and i['password'] == password :
                t = (datetime.datetime.now().day, datetime.datetime.now().month, datetime.datetime.now().year)
                if i['posts'] is None:
                    b = [t, x]
                    i['posts'] = b
                    break
                else:
                    g = [t, x]
                    i['posts'].append(g)


while True :
    try :
        sing = int(input('хотите войти (1) или зарегистрироваться (0)'))
    except :
        sing = 0

    if sing == 1 :
        login = input('введите логин')
        password = input('введите пароль')
        sin = Autor(login, password)
        if login != 'admin' and password != 'admin' :
            x = input('хотите написать пост? (1-да enter-нет)')
            if x == '1' :
                while True :
                    _time = (datetime.datetime.now().day, datetime.datetime.now().month, datetime.datetime.now().year)
                    data = input('напишите пост')
                    user = User.new_post(data)
                    y = input('хотите написать еще пост ? (1-да enter-нет)')
                    if y == '1' :
                        continue
                    else :
                        break
            else :
                pass
    elif sing == 0 :
        login = input('input login')
        password = input('input password')
        New = Reg(login, password)
        New._add()
