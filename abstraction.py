class Car:

    def start(self):
        self.__check_engine()
        print("Car started")

    def __check_engine(self):
        print("Checking engine...")


car = Car()

car.start()