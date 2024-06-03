# adding more attributes to the parent class
class Animal:
# -> none is a default value that is returned if no value is passed
    def __init__(self, sound ) -> None:
        self.sound = sound

    def make_sound(self) -> str:
        return f"the {type(self).__name__} goes {self.sound}"

class Dog(Animal):
    def make_sound(self) -> str:
        return f"{self.sound} {self.sound} ..................... {self.sound}"

class Cat(Animal):
    def make_sound(self) -> str:
        sound = f"The ugly  cat lets out a small"
        sound += f" {self.sound} {self.sound} {self.sound}"
        return sound

class Lion(Animal):
    def make_sound(self) -> str:
        return f"The fierce lion lets out a big {self.sound}!!!!"

class Person:
    def make_sound(self) -> str:
        return f"Hello, I am a person"

def sound(obj):
    # have functions that can apply to all different types of objects
    print(obj.make_sound())

animals = [Cat("tweet"), Dog("bark"), Lion("roar"), Person()]

for animal in animals:
    sound(animal)