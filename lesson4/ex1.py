from abc import ABC, abstractmethod
import datetime

d = []
_a = datetime.datetime.now().year


class Person(ABC) :
    def __init__(self, name, date) :
        self.name = name
        self._date = date

    @abstractmethod
    def years_old(self, a) :
        return a - self._date

    @abstractmethod
    def info(self) :
        return (f'фамиля : {self.name}, '
                f'дата рождения : {self._date}, ')


class Abitur(Person) :

    def __init__(self, name, date, please) :
        super().__init__(name, date)
        self._please = please
        d.append({'фамиля' : name, 'дата рождения' : date,
                  'факультет' : please})

    def years_old(self, a) :
        super().years_old(a)

    def info(self) :
        return (f'фамиля : {self.name}, '
                f'дата рождения : {self._date}, '
                f'факультет : {self._please} ')


class Stud(Person) :

    def __init__(self, name, date, please, course) :
        super().__init__(name, date)
        self._please = please
        self._course = course
        d.append({'фамиля' : self.name, 'дата рождения' : self._date,
                  'факультет' : self._please, 'курс' : self._course, })

    def years_old(self, a) :
        super().years_old(a)
        return a - self._date

    def info(self) :
        return (f'фамиля : {self.name}, '
                f'дата рождения : {self._date}, '
                f'факультет : {self._please}, '
                f'курс : {self._course}')


class Teacher(Person) :

    def __init__(self, name, date, please, dolg, years_work) :
        super().__init__(name, date)
        self._please = please
        self._dolg = dolg
        self._years_work = years_work
        d.append({'фамиля' : self.name, 'дата рождения' : self._date,
                  'факультет' : self._please, 'должность' : self._dolg, 'стаж' : self._years_work})

    def years_old(self, a) :
        super().years_old(a)

    def info(self) :
        return (f'фамиля : {self.name}, '
                f'дата рождения : {self._date}, '
                f'факультет : {self._please}, '
                f'должность : {self._dolg}, '
                f'стаж : {self._years_work}')


p1 = Abitur('Alex', 2001, 'DDD')
p2 = Abitur('Dima', 2002, 'NNN')
p3 = Stud('Vova', 2000, 'HHH', 1)
p4 = Stud('Artur', 2000, 'KKK', 2)
p5 = Teacher('Anna', 1974, 'JJJ', 'General', 25)
p6 = Teacher('Nataly', 1976, 'DDD', 'Old', 30)
print(p1.info())
print(p2.info())
print(p3.info())
print(p4.info())
print(p5.info())
print(p6.info())
print(f'{p3.name} {p3.years_old(_a)} years old')
print(d)
x = input()


def serch(x) :
    for i in d :
        f = _a - i['дата рождения']
        if str(f) == x :
            print(i)
        else :
            pass


serch(x)
