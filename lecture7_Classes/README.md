# Classes

Create a new file : New-Item -ItemType File -Name README.md

## Functions Recap

- finctions repeated/isolated block of code
- use parameter varable = input
- function scope: indicates access, can be global or not
- return statment -> return output

E.G.

```py
def add_number(num1, num2)
    result = num11 + num2
    reurn resullt
```

## OOP

- Object orientated programming
- organizing code around objects, which are self contained modules that contain both data and insturctions that operate on that data
- OOP promotes encapsulation -> bundling data and behaviour togethere within objects
- OOP promotes abstraction -> focuses on essential characteristics and behaviours of objects
- reduces code duplication
- Classes = blueprint for creating objects
  - define a set of atributes and methods that will be created in code
  - object is instance of code
- function withong the scope of a class is a method
- init method is a constroctor, called when an object is created from the class. Allows the class to initialize the attributes of the objects

```py
# class = blueprint for creating object, each class knows two things about itself ; attribute and method
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
print(cat_one.speak())
```

## What is OOP?

- procedural programming
- functional programming
- Even driven programming
- Logic Programming
- Modular Programming

## Classes in Python

- blueprint for creating objects
- defines a set of attributes and methods that the created objects of the class can use
- attributes = characteristics of an object
  - values that define the characteristic associated with an object
  - define state of an object and provide information about its current condition
  - methods created in a class are indented
- methods = operations that an object can perform. functions that behave to a class
  
## Objects in Python

## Four pillars of OOP

- Inheritance
  - Parent and child class
  - defines a class that inerits all the methods and properties from another class
- Polymorohism
  - access these overridden methods and attributes that share the same name as base class
- Encapsulation
  - Wrapping data(variables) and methods (functions) into a single unit (class)
  - restricting access to the direct modification of the objects attributes
- Abstraction
  - Concept of hiding the complex implementation details
  - showing only the essential features of the object
  - extension of encapsulation. Hiding complexity