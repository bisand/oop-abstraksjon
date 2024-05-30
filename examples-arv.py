from models.Car import Car
from models.ElectricCar import ElectricCar
from models.Lorry import Lorry

car = Car("Ford", "Explorer", 5)

print(car.make)

vehicle_list = [Car("Volvo", "XC90", 5), Lorry("Scania", "Something")]

for v in vehicle_list:
    print(v.make)

el_car = ElectricCar("Tesla", "Model 3", 4)

for v in ElectricCar.vehicles:
    print(v.__dict__)

Car.remove_vehicle(car)

for v in ElectricCar.vehicles:
    print(v.__dict__)


print(el_car.accellerate())
