class vehicle():
    def start(self):
        print("Vehicle is starting")
class car(vehicle):
    def drive(self):
        print("Car is driving")
car = car()
car.start()
car.drive()

