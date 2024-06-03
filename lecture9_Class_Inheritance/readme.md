# Inheritance

## what is inheritance

- create a new class and have it inherit attributes and properties from base class
- to get a class with the same attributes and properties as another class -> extending some of the nehaviour and adding attributes
- Parent/Base class : has what we want to inherit
- Child/SubClass

```py
#base class
class Animal:
    def __init__(self, sound: str) -> None:
        self.sound = sound
    
    def make_sound(self) -> str:
        print (f"the {type(self).__name__} goes {self.sound}")
# child class
class Lion(Animal):
    pass

animal = Animal("Animal sound")
lion = Lion ("rawr")

print(animal.make_sound())
print(lion.make_sound())
```

## method overiding

- same name inside the sub class
- can use super() function to extend method
- super().
- can call the base class and add extended behaviour

```py
#base class
class Animal:
    def __init__(self, sound: str) -> None:
        self.sound = sound
    # the > str shows what we should be reurning
    def make_sound(self) -> str:
        print (f"the {type(self).__name__} goes {self.sound}")
# child class
class Lion(Animal):
    def make_sound(self) -> str:
        return f"The fierce lion lets out a big {self.sound}!!!!"

animal = Animal("Animal sound")
lion = Lion ("rawr")

print(animal.make_sound())
print(lion.make_sound())
```

## Methods overiding and super()

- the main method we are overiding is __init__()
- we can use super().__init()
- to make sure we have the attributes in our parent class
- to protect attributes we want to keep

```py
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(person):
    # need to call a new init to add a new attribute
    def __init__(self, name, age):
        # so we call super to call to Person
        super().__init__(name, age)
        # adding grade attributes to the student 
        self.grades = []
```

```py
class BaseClass:
    #Base Class Definition
    def print_name(self):
        print(self.name)

class SubClass(BaseClass):
    #Subclass Definition
    def print_name(self)
    print("code before base method call.")
    super().print_name()
    print("code after base method call.")
```

## Multiple Ineritance

- can have 2 parent classes
- isinstance(object, ClassType) to see if object is from class type
- issubclass(SubClass, BaseClass) -> to see if something is a subclass of a specific class

```py
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age age

person = Person("peter", 20)
print(isinstance(person, Person)) # true
```

```py
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age age


class Student(Person):
    def __init__(self, name, age):
        # so we call super to call to Person
        super().__init__(name, age)
        # adding grade attributes to the student 
        self.grades = []

person = Student("peter", 20)
print(issubclass(Student, Person)) # true
```

## special methods

- make objects more functional with python
- characteristic is the __ befor and after the came (double underscore)
- helps expand functionality
- __init__() called when you construct a new object

## object as string

- __repr__()
- for representation
- returns a string for an official representaion of the object
- used for debugging
- will contain extra information
- or __str__()
- representation of our object when its cased to a string
- better for users

```py
class Student:
    def __init__(self, fullname, student_number):
        self.fullname = fullname
        self.student_number = student_number
    
    def __repr__(self):
        return f"Student({self.fullname}, {self.student_number})"

new_student = Student("Peter Jackson", "PJ323423")
```

```py
class Student:
    def __init__(self, fullname, student_number):
        self.fullname = fullname
        self.student_number = student_number
    
    def __str__(self):
        return f"Fullname:\t{self.fullname}\nStudent Num:\t{self.student_number}\n"

new_student = Student("Peter Jackson", "PJ323423")
print(new_student)
```

## special method and math

- __add__()
- x.__add__(y) is x+y

```py
class MyNumber:

    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return MyNumber(self.value + other.value)

num1 = MyNumber(10)
num2 = MyNumber(5)
num3 = num1 + num2
#num 1 = self , num2= other
print(num3.value)
```

## Container like-Objects

- special methods we use to work with dictionaries and list
- object[y] -> Object.__getitem__(y)
- get item in index
- length -> __len__(self)
- Get Item -> __getitem__(self, Key)
- Set Item -> __setitem__(self, Key, item)
- Contains Item -> __contains__(self, item)
- iterator -> __iter__(self)
- Next -> __next__(self)

```py
class ContactList:

    def __init__(self):
        self.contact_list = []

    def add_contact(self, contact):
        self.contact_list.append(contact)
    
    def __getitem__(self, key):
        return self.contact_list[key]

contact_list= ContactList()
contact_list.add_contact("test contact")
print(contact_list[0]) # output test contact

```

## comparators

- compare objects to greater than or less than 
- x>y -> x.__gt__(y)

```py
class Student:


    def __init__(self, fullname, student_number, average):
        self.fullname = fullname
        self.student_number = student_number
        self.average = average
    
    def __str__(self):
        return f"Fullname:\t{self.fullname}\nStudent Num:\t{self.student_number}\n"
    
    def __gt__(self, other):
        return self.average > other.average
        # student 1 is self and student 2 is other

student1 = Student("Peter Jackson", "PJ323423", 88)
student2 = Student("Jane Jackson", "PJ323423", 85)
print(student1> student2) # output: True
```

## polymorphism

- Thinking about the behaviour of an object and not the type
- only care about what it can do not what it is
- when we have differnt objects
- doesnt care what it is recieving
- e.g. print
- function takes in an object and doesnt care wht type of object it is
- we do it with method overiding
- Duck typing -> when you have an object with the same behaviour it can be used