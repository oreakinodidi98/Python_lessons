#base class


class Animal:
    def __init__(self, sound: str) -> None:
        self.sound = sound
    
    def make_sound(self) -> str:
        return f"The {type(self).__name__} goes {self.sound}"


# child class
class Lion(Animal):
    def make_sound(self) -> str:
        return f"The fierce lion lets out a big {self.sound}!!!!"

animal = Animal("Animal sound")
lion = Lion ("rawr")

print(animal.make_sound())
print(lion.make_sound())