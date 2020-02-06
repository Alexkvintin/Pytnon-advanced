class CM:
    def __init__(self, name, _type_):
        self._name = name
        self._type = _type_

    def __enter__(self):
        print('Работает !')
        try:
            self._file = open(self._name, self._type)
            print('Запись успешна !')
            return self._file
        except Exception as e:
            print('Возникла ошибка, ', e, 'файл был создан заново или очищен !')
            self._file = open(self._name, "w")
            return self._file

    def __exit__(self, exc_type, exc_value, exc_tr):
        self._file.close()


with CM('test.txt', 'a') as file:
    file.write('some text... ')
