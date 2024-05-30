class Vehicle:

    vehicles = []

    def __init__(self, make, model) -> None:
        self.make = make
        self.model = model

        Vehicle.vehicles.append(self)

    def remove_vehicle(self):
        Vehicle.vehicles.remove(self)