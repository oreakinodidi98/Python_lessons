class Animal:
# -> none is a default value that is returned if no value is passed
    def __init__(self, sound) -> None:
        self.sound = sound
    
    def make_sound(self) -> str:
        return f"the {type(self).__name__} says {self.sound}"

# child class
class Lion(Animal):
    pass

class Dog(Animal):
    pass

class Cat(Animal):
    pass

# creating instances of the classes
animal = Animal("woooooooow")
print(animal.make_sound())

dog = Dog("bark")
lion = Lion("roar")
cat = Cat("meow")


print(dog.make_sound())
print(lion.make_sound())
print(cat.make_sound())

# extending behaviour inside make sound method
class Lion(Animal):
    def make_sound(self) -> str:
        return f"The fierce lion lets out a big {self.sound}!!!!"
    
class Cat(Animal):
    def make_sound(self) -> str:
        sound = "The ugly cat lets out a small"
        sound += f" {self.sound} {self.sound} {self.sound}"
        return sound

class Dog(Animal):
    def make_sound(self) -> str:
        return f"{self.sound} {self.sound} ..................... {self.sound}"
    
dog = Dog("bark")
lion = Lion("roar")
cat = Cat("meow")


print(f"Reslts form adding additional functions:\n", dog.make_sound())
print(lion.make_sound())
print(cat.make_sound())

## extend classes by addind more attributes

class Lion(Animal):
# adding color attribute using the __init__ method and super() function
    def __init__(self, sound, color) -> None:
        # going to the innit of animal class and calling it
        super().__init__(sound)
        #dont need a self.sound = sound because the sound is already being passed to the parent class
        self.color = color
        self.weight = "200kg"

    def make_sound(self) -> str:
        return f"The fierce {self.color} lion lets out a big {self.sound}!!!!"
    
    

lion = Lion("roar", "golden")


print(f"\nResults from adding color attribute:\n")
print(lion.make_sound())
print(lion.color)
print(lion.sound)
print(lion.weight)

