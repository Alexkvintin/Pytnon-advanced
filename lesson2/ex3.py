class T:
    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z

    def addition(t1, t2):
        return dict(x = t1['x'] + t2['x'],
                    y = t1['y'] + t2['y'],
                    z = t1['z'] + t2['z']
                    )

    def subtraction(t1, t2):
        return dict(x=t1['x'] - t2['x'],
                    y=t1['y'] - t2['y'],
                    z=t1['z'] - t2['z']
                    )

    def division(t1, t2):
        return dict(x=t1['x'] / t2['x'],
                    y=t1['y'] / t2['y'],
                    z=t1['z'] / t2['z']
                    )

    def multiplication(t1, t2):
        return dict(x=t1['x'] * t2['x'],
                    y=t1['y'] * t2['y'],
                    z=t1['z'] * t2['z']
                    )

    def info_t(self):
        return dict(
            x = self._x,
            y = self._y,
            z = self._z
        )


t1 = T(3, 4, 5)
t2 = T(2, 3, 4)
print(T.addition(t1.info_t(), t2.info_t()))
print(T.subtraction(t1.info_t(), t2.info_t()))
print(T.division(t1.info_t(), t2.info_t()))
print(T.multiplication(t1.info_t(), t2.info_t()))
