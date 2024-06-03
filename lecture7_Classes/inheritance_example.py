# working with base class and child class
class Animal:
    # if i didnt define init, it will be implicitly created 
    # def __init__(self, name):
    #     self.name = name
    def eat(self):
        # pass acts as a placeholder, to avoid error
        pass


class dog(Animal):
    def eat(self):
        return("Dog eats meat")


class cat(Animal):
    def eat(self):
        return("Cat eats fish")
    

my_dog = dog()
my_cat = cat()
print(my_dog.eat())
print(my_cat.eat())