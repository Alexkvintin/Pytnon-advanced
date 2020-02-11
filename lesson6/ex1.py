class List:
    def __init__(self, *args):
        self._list = [*args]

    def append(self, item):
        self._list.append(item)
        return f'Был добавлен елемент {self._list[-1]}'

    def pop(self, number):
        return f'Был удален елемент {self._list.pop(number)}, по адрессу {number}'

    def clear(self):
        self._list = []
        return 'Список очищен'

    def remove(self, item):
        self._list.remove(item)
        return f'Был удален елемент {item}'

    def insert(self, number, item):
        self._list.insert(number, item)
        return f'Был добавлен елемент {item}, по адрессу {number} '

    def __str__(self):
        return str(self._list)

    def __add__(self, other):
        for values in other:
            self.append(values)
        return f'Были добавлены {other}'


l = List(1, 2, 3, 4)
print(l)
print(l.pop(2))
print(l)
print(l.append('5'))
print(l)
print(l.insert(0, 'name'))
print(l)
print(l.remove('name'))
print(l)
print(l.clear())
print(l)
p = [1, 2, 4]
l.append(4)
print(l+p)
print(l)
