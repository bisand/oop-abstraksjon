from models.Car import Car


class ElectricCar(Car):

    def __init__(self, make, model, doors) -> None:
        super().__init__(make, model, doors)

    def accellerate(self):
        return "This electric car is accellerating fast and silently!!"