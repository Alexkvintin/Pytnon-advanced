class T:
    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z

    def __add__(self, other):
        return dict(
            x=self._x + other._x,
            y=self._y + other._y,
            z=self._z + other._z
        )

    def __sub__(self, other):
        return dict(
            x=self._x - other._x,
            y=self._y - other._y,
            z=self._z - other._z
        )

    def __truediv__(self, other):
        return dict(
            x=self._x / other._x,
            y=self._y / other._y,
            z=self._z / other._z
        )

    def __mul__(self, other):
        return dict(
            x=self._x * other._x,
            y=self._y * other._y,
            z=self._z * other._z
        )

    def info_t(self):
        return dict(
            x = self._x,
            y = self._y,
            z = self._z
        )


t1 = T(3, 4, 5)
t2 = T(2, 3, 4)
print(t1.__add__(t2))
print(t1.__sub__(t2))
print(t1.__mul__(t2))
print(t1.__truediv__(t2))
