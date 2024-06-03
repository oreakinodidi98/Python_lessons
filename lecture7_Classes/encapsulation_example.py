class Car:
    def __init__(self):
        # __speed is a private variable because it has two underscores
        self.__speed = 100

    def accelerate(self):
        self.__speed += 5
        
    def get_speed(self):
        return self.__speed
    

my_car = Car()

my_car.accelerate()

print(my_car.get_speed())