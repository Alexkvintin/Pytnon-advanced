class Car:

    def __init__(self, num_of_doors, num_of_wheels, brand):
        self._num_of_doors = num_of_doors
        self._num_of_wheels = num_of_wheels
        self._brand = brand


class LightCar(Car):

    def __init__(self, num_of_doors, num_of_wheels, brand, model, speed ):
        super().__init__(num_of_doors, num_of_wheels, brand)
        self._speed = speed
        self._model = model

    def car_info(self):
        return dict(
            brand = self._brand,
            model = self._model,
            speed = self._speed,

        )


class Truck(Car):

    def __init__(self, num_of_doors, num_of_wheels, brand, model, weight):
        super().__init__(num_of_doors, num_of_wheels, brand)
        self._weight = weight
        self._model = model

    def car_info(self):
        return dict(
            brand = self._brand,
            weight = self._weight,
            model = self._model
        )


car1 = LightCar(4, 4, 'audi', 's4', 400)
car2 = Truck(2, 6, 'ГАЗ', 'k3', 2)
print(car1.car_info())
print(car2.car_info())
