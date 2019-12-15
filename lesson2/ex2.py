class Mag:
    def __init__(self, name, quantity_sold):
        self._name = name
        try:
            self._quantity_sold = int(quantity_sold)
        except ValueError:
            print('Количество должно быть целым числом !')
            self._quantity_sold = 0

    def sold(self, new_sold):
         try:
             self._quantity_sold = self._quantity_sold + new_sold
         except TypeError:
             print('Значение должно быть целым числом !')


    def mag_info(self):
        return dict(
            name=self._name,
            quantity_sold=self._quantity_sold)

    def sum_(*x):
       a = 0
       for i in x:
           a+=i
       return f'общее количество продаж : {a}'


mag1 = Mag('allo', '4a')
print('-'*80)
print(mag1.mag_info())
print('-'*80)
mag2 = Mag('ttt', 12)
print(mag2.mag_info())
print('-'*80)
mag3 = Mag('rozetka', 30)
print(mag3.mag_info())
print('-'*80)
mag1.sold(2)
print(mag1.mag_info())
print('-'*80)
mag2.sold('r')
print(mag2.mag_info())
print('-'*80)
mag3.sold(0)
print(mag3.mag_info())
print('-'*80)
print(Mag.sum_(mag1._quantity_sold, mag2._quantity_sold, mag3._quantity_sold))
