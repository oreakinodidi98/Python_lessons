# instances, Static and class methods

## classes recap

- classes = blue print for creating objects
- defines attributes and methods all the objects will have
- e.g Blue print for building a hous = **class**
- classes need attributes and metods
- **methods** = behaviours -> e.g. set location, opening doors, turni on lights, cleaning  -> functions underneath a class
- **house** = object
- **attributes** = define the state of the object-. characteristics or properties -> number of bedrooms, colour or years built
- **objects** = refered to instances -> results or instances of the class created -> object is actuall product , so house built of the blueprint actually provided

## atribute

## instance Methods

- actions or behaviours that specific objects can perform
- defined withing the class
- model how objects interact and behave
- so functions we have been using
- class = student
- __init__ (constructor method)
- attribute = name 
- use self key word to match parameter
- good to make sure parameter name = attribute name
- self keyword, lets objects have access to methods and attributes bellonging to class
- Instance method = study
- these belong to the object
- each object created from class hass access to the instance method

```py
class student:
    # constructor
    def __init__(self, name):
        self.name = name
# instance method, accessibl by all the objects in the particular class 
    def study (self)
        print(f"{self.name} is studying hard !)

# creating a student object
student1= student("Ore")

# calling the instance method
student1.study()
```

## static methods

- stand alone functions associated with class
- useful for organising utility functions that are related to the class
- but dont depend on individual object instances
- can group togethere related functionalities withing a class
- calling static method when in the class
- decarator = tools that allow us to modify the behaviour of function
  - will allow the function to be accessed by the user as long as they pass in the class name
- Only use as utility functions
- Wrapper around function
- e.g. a cook book class
  - will have a pancake recipe as a static method
  - so anyone can come in use the recipe

```py
class MathUtil:
    @staticmethod
    def add(a, b):
        return a + b
    
# calling the static method
result = MathUtil.add(2, 3)
print(f"Result of {3} + {2}= {result}")
```

## Class Methods

- in OOP Class methd is like a special function that belongs to the class itself
- define functions that operate on the class itself
- like functions that operate on the class itself rather than individual objects
- usefull for modefying class attributes or performing operations that involve the class as a whole
- recieve the CLS
- modify and access class level data
- only way to chang a class variable is through a class method

```py
class MathUtil:
    @classmethod
    def calculate_average(cls, num_list):
        total = sum(num_list)
        return total / len(num_list)

# using class method
numbers = [10, 20, 30, 40, 50 ,60]
average = MathUtil.calculate_average(numbers)
print(average)
```