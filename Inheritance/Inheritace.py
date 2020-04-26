class Vehicle:
    def general_usage(self):
        print("general use: trnasportation")


class Car(Vehicle):
    def __init__(self):
        print("I am a car")
        self.wheels=4
        self.has_roof=True

    def specific_usage(self):
        print("comute to work")


class MotorCycle(Vehicle):
    def __init__(self):
        self.wheels=4
        self.has_roof=True

    def specific_usage(self):
        print("road trip and racing")



car=Car()
car.general_usage()


