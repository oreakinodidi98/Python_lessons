class MathUtil:
    @classmethod
    def calculate_average(cls, num_list):
        total = sum(num_list)
        return total / len(num_list)

# using class method
numbers = [10, 20, 30, 40, 50 ,60]
average = MathUtil.calculate_average(numbers)
print(average)

#  Example 2

class Gamers:
    total_people = 0
# constructor method
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # as the user creates a new object, the total_people increases by 1
        Gamers.total_people += 1

    @classmethod
    def display_total_people(cls):
        print(f"There has been {cls.total_people} gamer created so far")

# input name and age of person
name = input("Enter the name of the Gamer: ")
age = int(input("Enter the age of the Gamer: "))
# create object
gamer_one = Gamers(name, age)
gamer_two = Gamers("Tom", 30)
# display total people
Gamers.display_total_people()

# Example 3

class pokemon:
    total_pokemon = 0
    all_pokemon = []

    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.moves = []
        pokemon.total_pokemon += 1
    # instance methods = functions that belong to the class
    def add_move(self, pokemon_move):
        self.moves.append(pokemon_move)
        print(f"{self.name} has learned {pokemon_move}")

    @classmethod
    def display_total_pokemon(cls):
        print(f"There has been {cls.total_pokemon} pokemon created so far")
        for pokemon in cls.all_pokemon:
            print(f"current Pokemon is:{pokemon.name}")

    @staticmethod
    def calc_damage(att, deff):
        return att - deff

pikacho = pokemon("Pikachu", 10)
cario = pokemon("Lucario", 15)
bulbasaur = pokemon("Bulbasaur", 5)

pikacho.add_move("Thunderbolt")
pikacho.add_move("Quick Attack")
pikacho.add_move("Iron Tail")
cario.add_move("Aura Sphere")
cario.add_move("Dragon Pulse")
bulbasaur.add_move("Vine Whip")
bulbasaur.add_move("Solar Beam")

pokemon.all_pokemon.append(pikacho)
pokemon.all_pokemon.append(cario)
pokemon.all_pokemon.append(bulbasaur)

print(pikacho.moves)
pokemon.display_total_pokemon()

damage = pokemon.calc_damage(50, 20)
print(f"Damage caused is {damage}")

