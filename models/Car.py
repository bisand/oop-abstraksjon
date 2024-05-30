from models.Vehicle import Vehicle


class Car(Vehicle):

    def __init__(self, make, model, doors) -> None:
        super().__init__(make, model)
        self.doors = doors

    def accellerate(self):
        return "The car is accellerating!"