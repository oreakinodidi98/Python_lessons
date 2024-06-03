# working with base class and child class
class Animal:
    # if i didnt define init, it will be implicitly created 
    def eat(self):
        # pass acts as a placeholder, to avoid error
        pass


class dog(Animal):
    def eat(self):
        return("Dog eats meat")


class cat(Animal):
    def eat(self):
        return("Cat eats fish")
    

def make_food(animal):
    return animal.eat()


my_dog = dog()
my_cat = cat()

print(my_dog.eat())
print(my_cat.eat())

print(make_food(my_dog))
print(make_food(my_cat))