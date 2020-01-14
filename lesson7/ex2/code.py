import sqlite3

try:
    conn = sqlite3.connect('inst.db')
except:
    print('нет такой базы данных !')
cursor = conn.cursor()


class Autor:
    def __init__(self, login, password):
        self._login = login
        self._password = password


class Admin(Autor):
    def __init__(self, login, password):
        super().__init__(login, password)
        self._login = login
        self._password = password

    def add_new(self, list_to_add):
        conn = sqlite3.connect('inst.db')
        cursor = conn.cursor()
        cursor.execute(f'INSERT INTO students(plase, grupe, points, num) VALUES(?, ?, ?, ?)', list_to_add)
        conn.commit()
        conn.close()

    def upd(self, num, plase, grupe, points):
        cursor.execute(f'UPDATE students SET plase = {plase}, grupe = {grupe}, points = {points} WHERE num = {num}')


class User(Autor):
    def __init__(self, login, password):
        super().__init__(login, password)
        self._login = login
        self._password = password

    def _all(self):
        conn = sqlite3.connect('inst.db')
        cursor = conn.cursor()
        cursor.execute('SELECT plase, grupe, points, num FROM students ')
        print(cursor.fetchall())
        conn.close()

    def better(self, points):
        conn = sqlite3.connect('inst.db')
        cursor = conn.cursor()
        cursor.execute('SELECT plase, grupe, points, num FROM students WHERE points >= ?', points)
        print(cursor.fetchall())
        conn.close()

    def _search(self, num):
        conn = sqlite3.connect('inst.db')
        cursor = conn.cursor()
        cursor.execute('SELECT plase, grupe, points, num FROM students WHERE num = ?', num)
        print(cursor.fetchall())
        conn.close()


while True:
    logining = Admin(input('vvedite login'), input('vvedite password'))
    if logining._login == 'admin' and logining._password == 'admin':
        logining = Admin('admin', 'admin')
        p = input('добавить студента(1) или редактировать(2), выход(enter) ')
        if p == '1':
            pla = input('факультет')
            gru = input('группа')
            poi = input('количество балов')
            num = input('номер билета')
            logining.add_new(list_to_add=(pla, gru, poi, num))

        elif p == '2':
            num = input('номер билета')
            pla = input('факультет')
            gru = input('группа')
            poi = input('количество балов')
            logining.upd(num, pla, gru, poi)
        else:
            break

    else:
        logining = User(' ', ' ')
        print('')
        menu = input("""выберите действие 
                показать список отличников (1)
                поиск определенного студнта по номеру (2)
                список всех студентов (3)
                выход (enter)                """)
        if menu == '1':
            try:
                logining.better(points=(input('введите минимальный балл отличника: '),))
            except:
                print('нет студентов с такими оценками')
        elif menu == '2':
            try:
                logining._search(num=(input('введите номер студенческого: '),))
            except:
                print('такого студента нет !')
        elif menu == '3':
            logining._all()
        else:
            break

conn.close()
