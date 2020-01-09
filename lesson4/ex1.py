from abc import ABC, abstractmethod
import datetime

a = 2019

class Person(ABC):

    @abstractmethod
    def __init__(self, name, date):
        self._name = name
        self._date = date

    @abstractmethod
    def years_old(self):
        return self._date - a

    def info(self):
        return dict


class Abitur(Person):
    def __init__(self, name, date, please):
        super().__init__(name, date)
        self._please = please

    def years_old(self):
        super().years_old()


class Stud(Person):
    def __init__(self, name, date, please, course):
        super().__init__(name, date)
        self._please = please
        self._course = course

    def years_old(self):
        super().years_old()


class Teacher(Person):
    def __init__(self, name, date, please, dolg, years_work):
        super().__init__(name, date)
        self._please = please
        self._dolg = dolg
        self._years_work = years_work

    def years_old(self):
        super().years_old()


p1 = Abitur('Alex', 2001, 'DDD')

p2 = Abitur('Dima', 2002, 'NNN')
p3 = Stud('Vova', 2000, 'HHH', 1)
p4 = Stud('Artur', 2000, 'KKK', 2)
p5 = Teacher('Anna', 1974, 'JJJ', 'General', 25)
p6 = Teacher('Nataly', 1976, 'DDD', 'Old', 30)

x=input()
print(p1.info())
dict = {1:2, 3:5}
print(dict[1])
def search_(x):
    if Person.info(p1)['data'] == x:
        print(Person.info(p1))

search_(x)
