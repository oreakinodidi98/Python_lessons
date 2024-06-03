# class = blueprint for creating object, each lass knows two things about itself ; attribute and method
# instance / oject - this hre is the instance or object created from the class

class Cat:
    # method = Function withing the class
    # init method is a constroctor, called when an object is created from the class. 
    # Allows the class to initialize the attributes of the objects which are created
    # self referes to the instance calling the method - implicit pointer
    def __init__(self, user_given_name, user_given_age, user_given_color):
        self.name = user_given_name
        self.age = user_given_age
        self.color = user_given_color
    # the class cat has 3 attributes name, age and color
        # user_given_name is the parameter the user will give when creating the object
    def speak(self):
        return(f"{self.name} says meowwwwwwwwwwwwwww")
    
# an object is an instantiation of a class
    
cat_one = Cat("Garfield", 50, "orange")
cat_two = Cat("Tom", 33, "grey")
cat_three = Cat("Sylvester", 41, "black")
cat_four = Cat("Simba", 25, "golden")
        
print(cat_one.name)
print(cat_three.speak())
print(cat_two.speak())
# can make user create an object 
input_name = input("Enter the name of the cat: ")
input_age = input("Enter the age of the cat: ")
input_color = input("Enter the color of the cat: ")
cat_five = Cat(input_name, input_age, input_color)
print(cat_five.speak())

## example 2
class vehicle:
    # always call the innit , as it is constructor
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
    def speed(self):
        return(f"{self.make} vehicle can go 0-60 in 5 seconds")
    def display(self):
        return(f"This is a {self.color} {self.year} {self.make} {self.model}")

car_one = vehicle("Toyota", "Corolla", 2020, "red")
car_two = vehicle("Ford", "Focus", 2019, "blue")
print(car_one.speed())
print(car_two.display())
print(car_one.display())

# make user create vehicle object
input_make = input(str("What is the make of the vehicle: "))
input_model = input(str("What is the model of the vehicle: "))
input_year = int(input("What is the year of the vehicle: "))
input_color = input(str("What is the color of the vehicle: "))

car_three = vehicle(input_make, input_model, input_year, input_color)
print(car_three.display())
print(car_two.make)
print(f"{car_two.make} {car_two.model} is a {car_two.year} model")