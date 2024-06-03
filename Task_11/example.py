# parent clas for a car which can be inherited by other classes
class Car:
    # class variable for weather the engine is on or off
    is_running = False

    #constructor that allos us to set the make, model and year of the car
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    # method to start the engine
    def start_car(self):
        self.is_running = True
        print(f"car is on")
    
    #method to stop the engine
    def stop_car(self):
        self.is_running = False
        print(f"car is off")

    # mehod to print make and model of the car
    def display_car(self):
        print(f"This vehicle is a {self.make} {self.model}, produced in {self.year}")
    
# inheriting all atributes and methods from the parent class Car and passing it as an argument to the pickuptruck class
class PickupTruck(Car):
    #this is an additional class variable that is unique to the pickup truck class
    is_loaded = False
    #method to load the truck
    def load(self):
        self.is_loaded = True
        print(f"Truck is loaded")
        #method to unload the truck
    def unload(self):
        self.is_loaded = False
        print(f"Truck is unloaded")

# create a pickup truck object
truck1 = PickupTruck("Ford", "F150", 2021)
# call the load method created in the pickup truck class (child class)
truck1.load()
# call the start car method created in the car class (parent class)
truck1.start_car()
# print out values to see if both of the above methods worked
print(truck1.is_loaded)
print(truck1.is_running)

truck1.display_car()