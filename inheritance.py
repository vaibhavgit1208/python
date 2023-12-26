class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

    def drive(self):
        print(f"This {self.vehicle_type} is being driven.")

class Car(Vehicle):
    def honk(self):
        print("Beep beep!")

class Truck(Vehicle):
    def load_goods(self):
        print("Loading goods...")

# Creating instances
car = Car("Car")
truck = Truck("Truck")

# Using methods from parent and child classes
car.drive()
car.honk()

truck.drive()
truck.load_goods()
