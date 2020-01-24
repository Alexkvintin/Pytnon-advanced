from mongoengine import *
import random


class Studs(Document):
    fullname = StringField(min_length=4, max_length=60)
    grupe = DecimalField(min_value=101)
    fakult = StringField(min_length=1, max_length=8)
    mark = ListField()
    cure = ReferenceField('Preps')

    def __str__(self):
        return self.fullname

    def get_stud_core(self):
        return self.cure

    def _sum(self):
        return sum(self.mark)


class Preps(Document):
    fullname = StringField(min_length=3, max_length=60)

    def __enter__(self):
        self._id = self.fullname


if __name__ == "__main__":
    connect('db_exmp1')
    "1"
    Preps.objects.delete()
    Studs.objects.delete()
    prep1 = Preps(
        fullname='Charles'
    ).save()
    prep2 = Preps(
        fullname='Sarah Connor'
    ).save()
    stud = Studs(
        fullname='Alicia',
        grupe=112,
        fakult='FA',
        mark=[60, 60, 70, 60],
        cure=prep1
    ).save()
    stud1 = Studs(
        fullname='Mateo',
        grupe=112,
        fakult='FA',
        mark=[60, 85, 76, 80],
        cure=prep1
    ).save()
    stud2 = Studs(
        fullname='Grace',
        grupe=231,
        fakult='FRA',
        mark=[60, 65, 67, 65],
        cure=prep2
    ).save()
    stud3 = Studs(
        fullname='Dani Ramos',
        grupe=231,
        fakult='FRA',
        mark=[80, 90, 75, 80],
        cure=prep2
    ).save()
    super = Studs.objects.filter(fakult='FRA', mark__gte=70)
    print(super)
    cure = Studs.objects.filter(cure=prep1)
    print(cure)
    "update"
    Studs.objects(fullname='Dani Ramos').update(mark=100)
    print(Studs.objects(fullname='Dani Ramos').to_json())
    "read"
    a = input('stud fullname')
    print(Studs.objects(fullname=a).to_json())
    "delete"
    Studs.objects(fullname='Dani Ramos').delete()
    print(Studs.objects.to_json())
    "create"
    azb = []
    Studs.objects.create(
        fullname='Dani Ramos',
        grupe=231,
        fakult='FRA',
        mark=[80, 90, 75, 80],
        cure=prep2

    )
    print(Studs.objects.to_json())
