# Classes

Create a new file : New-Item -ItemType File -Name README.md

- class = template/blueprint of what you want the object to look like
- defines the attributes and methods that all objects of that class will have

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

## Attributes

- Attributes are values that define the characteristics associated with an object
- define the state of an object and provide information about its current condition
- E.G. Class name house
  - attributes = Number of bedroom, year built

## Methonds

- define the actions or behaviours that objects can perform
- E.G. class named ‘House’, some relevant method could be
  - set_location(): Allows updating the location of the house

## constructor

- Special method that gets called when an object is created

```py
def __init__(self, name, age, graduated):
  self.name = name
  self.age = age
  self.graduated = graduated
```

## Destructor

- A destructor is a special method that gets called when an object is about to be destroyed. It is used to perform clean-up operations

```py
def __del__(self):
  print(f"{self.name} {self.age} {self.graduated} destroyed")
```

## Creating a class

- __init__ ( ) method is called when the class is instantiated
- The Class bellow takes in three values: a name, age and graduation status.
- When you instantiate a class, you create an instance or an object of that class

```py
class Student:

  def __init__(self, name, age, graduated):
    self.name = name
    self.age = age
    self.graduated = graduated

luke = Student("luke Skywalker", 23 , true)
```

```py
class House:

  def __init__(self, location):
    self.location = location
  
  def change_location(self, new_location):
    self.location = new_location
    

house = House('london')
house.change_location('Dartford')
```

## access control - Attributes

```py
class MyClass:

  def __init__(self):
    #public attribute
    self.public_attribute ="i am Public"

    # protected attribute (by convention)
    self._protected_attribute ="i am protected"

    # Private attributee
    self.__private_attribute= "i am Private"
```

## access control - Methods

```py
def public_method(self):
   #public method - can call from outside class
   return "this is a public method"

def _protected_method(self):
   #protected method - can call from outside class , but dont want you to 
   return "this is a protected method"

def __private_method(self):
   #private method - can not call from outside class
   return "this is a private method"
```

## applying the Access control

```py
# create instance of my class
obj = MyClass()

# Accessing public attributes and methods
print(obj.public_attribute) # output: I am public
print(obj.public_method()) # output: this is a public method

# Accessing protected attributes and methods
print(obj._protected_attribute) # output: I am protected
print(obj._protected_method()) # output: this is a protected method

# accessing prvate attributes and methods (name mangling applied)
# Note: it is still possible to access, but discuraged
print(obj._MyClass__private_attribute) # output: I am private
print(obj._MyClass__private_method()) # output: this is a private method
```

## Abstraction

```py
class Animal:
  def __init__(self, name, sound):
    self.name=name
    self.sound=sound
  
  def make_sound(self):
    raise NotImplementedError("Subclass must implement the make_sound method")

class Dog(Animal):
  def make_sound(self):
    return f"{self.name} says: {self.sound}"

class Cat(Animal):
  def make_sound(self):
    return f"{self.name} says: {self.sound}"

# usage
rover = Dog("rover", "woof")
tony = Cat("tony", "meow")

print(rover.make_sound())
print(tony.make_sound())
```

## polymorhism

- ability of different objects to respond to the same message or method call in different ways

## Method Oveiding and Super()

```py
class Person:

  def __init__(self, name, surname):
    self.name = name
    self.surname = surname

class Student(person):

  def __init__(self, name, surname):
    #copying the method of the parent and adding to it
    super().__init__(name, surname)
    self.grades=[]
```

- we copy __init__() from the parent class to set the values for the attributes “name” and “surname” and then extend it with attribute “grade”

## dunder methods

- Double underscore methods are special methods in Python
- part of method overiding