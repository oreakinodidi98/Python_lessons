
# adding more attributes to the parent class
class Animals:
# -> none is a default value that is returned if no value is passed
    def __init__(self, sound , colour) -> None:
        self.sound = sound
        self.colour = colour
    
    def make_sound(self) -> str:
        return f"the {type(self).__name__} says {self.sound}"
    
class Cat(Animals):
    def __init__(self, sound) -> None:
        super().__init__(sound, "ginger")
        self.speed = "2mph"
    
    def make_sound(self) -> str:
        sound = f"The ugly {self.colour} cat lets out a small"
        sound += f" {self.sound} {self.sound} {self.sound}"
        sound += f" and runs at {self.speed}"
        return sound

print(f"\nResults from adding more attributes to the parent class and sub class:\n")
cat = Cat("tweet")
print(cat.make_sound())
print(cat.colour)
print(cat.sound)
print(cat.speed)