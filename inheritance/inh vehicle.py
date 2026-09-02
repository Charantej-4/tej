class Vehicle:
    def start(self):
        print("Vehicle is starting")
class Car(Vehicle):
    def start(self):
        super().start()
        print("Car is ready to drive")
c1 = Car()
c1.start()