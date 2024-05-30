def greetings(name, greeting="Hello"):
    print(f"{greeting} {name}")


greetings("André")
greetings("André", "Goodbye")


class Animal:
    def sound(self, extra=""):
        return f"Some generic animal sound {extra}"


class Dog(Animal):
    def sound(self, extra=""):
        return f"Woff! {extra}"


class Cat(Animal):
    def sound(self, extra=""):
        return f"Miau... {extra}"


puddel = Dog()
rottweiler = Dog()

cat = Cat()
cat2 = Cat()

print(puddel.sound())
print(puddel.sound("Mjau"))
print(rottweiler.sound())
print(rottweiler.sound("Grrrrrrr!"))
print(cat.sound())
print(cat2.sound("pip"))


def summarize(a: int, b: int):
    return a + b


print(summarize(10, 5))
print(summarize(3.14, 2.56))
print(summarize("Python ", "rules!"))


class Vehicle:
    def drive(self):
        return "The vehiche is driving!"


class Car(Vehicle):
    def drive(self):
        return "The car is driving..."


class Bus(Vehicle):
    def drive(self):
        return "The bus is driving."


def drive_vehicle(vehicle: Vehicle):
    print(vehicle.drive())


vehicle = Vehicle()
car = Car()
bus = Bus()

drive_vehicle(vehicle)
drive_vehicle(car)
drive_vehicle(bus)
