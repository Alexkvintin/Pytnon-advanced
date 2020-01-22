from mongoengine import *
import random


class Studs(Document):
    fullname = StringField(min_length=4, max_length=60)
    grupe = DecimalField(min_value=101)
    fakult = StringField(min_length=1, max_length=8)
    mark = ReferenceField('Marks')
    cure = ReferenceField('Prep')


class Preps(Document):
    fullname = StringField(min_length=3, max_length=60)


class Marks(Document):
    marks = []
    mark = DecimalField(min_value=0)


if __name__ == "__main__":
    connect('db_exmp')
    "1"
    prep1 = Preps(
        fullname='Charles'
    )
    prep2 = Preps(
        fullname='Sarah Connor'
    )
    "2"
    marks = Marks
    for i in range(5) :
        marks.marks.append(random.randint(60, 100))
    marks.mark = 0
    for i in marks.marks :
        marks.mark += i
    marks.mark = marks.mark / 5
    stud = Studs(
        fullname='Alicia',
        grupe=112,
        fakult='FA',
        mark=marks.mark,
        cure=prep1
    )
    marks1 = Marks
    for i in range(5) :
        marks1.marks.append(random.randint(60, 100))
    marks1.mark = 0
    for i in marks1.marks :
        marks1.mark += i
    marks1.mark = marks.mark / 5
    stud1 = Studs(
        fullname='Mateo',
        grupe=112,
        fakult='FA',
        mark=marks1.mark,
        cure=prep1
    )
    marks2 = Marks
    for i in range(5) :
        marks2.marks.append(random.randint(60, 100))
    marks2.mark = 0
    for i in marks2.marks :
        marks2.mark += i
    marks2.mark = marks.mark / 5
    stud2 = Studs(
        fullname='Grace',
        grupe=231,
        fakult='FRA',
        mark=marks2.mark,
        cure=prep1
    )
    marks3 = Marks
    for i in range(5) :
        marks3.marks.append(random.randint(60, 100))
    marks3.mark = 0
    for i in marks3.marks :
        marks3.mark += i
    marks3.mark = marks.mark / 5
    stud3 = Studs(
        fullname='Dani Ramos',
        grupe=231,
        fakult='FRA',
        mark=marks3.mark,
        cure=prep1
    )

    print(stud1.mark)
