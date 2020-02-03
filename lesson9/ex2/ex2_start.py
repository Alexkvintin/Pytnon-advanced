from mongoengine import *
from ex2_rand import RandStud
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
    prep_id = StringField(min_length=0, max_length=9)
    fullname = StringField(min_length=3, max_length=60)

    def __str__(self):
        self._id = self.fullname


rand = RandStud()
if __name__ == "__main__":
    connect('db_exmp1')
    "1"
    Preps.objects.delete()
    Studs.objects.delete()
    prep_list = []
    for i in range(10):
        prep = Preps(
            fullname=rand.cure()
        ).save()
        prep_list.append(prep)
    for i in range(100):
        stud = Studs(
            fullname=rand.fullname(),
            grupe=rand.grupe(),
            fakult=rand.fakult(),
            mark=rand.mark(),
            cure=prep_list[random.randint(0, 9)]
        ).save()
