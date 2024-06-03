# ask for user input for name, age, hair colour and eye colur of a person
name= input("Enter the name of the person: ")
age = int(input("Enter the age of the person: "))
hair_color = input("Enter the hair color of the person: ")
eye_color = input("Enter the eye color of the person: ")


# create a class called person
class Person:
    
    def __init__(self, name, age, hair_color, eye_color):
        self.name = name
        self.age = age
        self.hair_color = hair_color
        self.eye_color = eye_color

    # method called can_drive to print out name of the person and that they are old enough to drive
    def can_drive(self):
        if self.age >= 18:
            print(f"{self.name} is old enough to drive")
        else:
            print(f"{self.name} is not old enough to drive")

# create subclass name child that has the same attibutes but overides can drive() method
class Child(Person):
    def can_drive(self):
        print(f"{self.name} is too young to drive")

# if age is 18 or older, create instance of adult class
if age >= 18:
    adult = Person(name, age, hair_color, eye_color)
    adult.can_drive()
# if age is less than 18, create instance of child class
else:
    child = Child(name, age, hair_color, eye_color)
    child.can_drive()