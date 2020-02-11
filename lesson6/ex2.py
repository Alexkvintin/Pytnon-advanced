class Dict:
    def __init__(self, **kwargs):
        self._dict = kwargs

    def __str__(self):
        return str(self._dict)

    def get(self, key):
        if key not in self._dict:
            print(f'Нет ключа \'{key}\'')
        else:
            return f'Значение ключа \'{key}\': {self._dict[key]}'

    def items(self):
        temp = []
        for i in self._dict:
            temp.append([i, self._dict[i]])
        return f'Возвращены пары (ключ, значение): {temp}'

    def keys(self):
        temp = []
        for i in self._dict:
            temp.append(i)
        return f'Ключи словаря {temp}'

    def values(self):
        temp = []
        for i in self._dict:
            temp.append(self._dict[i])
        return f'Значения словаря {temp}'

    def __add__(self, other):
        for i in self._dict:
            if i in other:
                print(f'{i}, уже усть в первом словаре !')
        for i in other:
            self._dict[i] = other[i]
        return self._dict


print('='*60)
d = Dict(один=1, два=2, три=3)
print(d)
print(d.get('десять'))
print(d.get('один'))
print(d.items())
print(d.keys())
print(d.values())
d2 = {'три': 3, '123': 123, '456': 123, 'два': 890}
print(d + d2)
