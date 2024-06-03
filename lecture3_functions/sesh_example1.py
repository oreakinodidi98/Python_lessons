# random function 

global_poke = "pikachu"

def poke_in_bag(poke1 , poke2):
    """This function prints the value of the global variable global_poke."""
    print(f"pokwmon 1: {poke1}. \npokemon 2: {poke2}.")
    print(f"you have an additional pokemon in bag: {global_poke}")


poke_in_bag("charmander", "bulbasaur")
#pythin reads from top to buttom, storres code at the top

#example 2
def my_function():
    """This function prints the value of the global variable global_poke."""
    global y 
    y = "this is a global variable withing my function"
    print(y)

my_function()
print(y)

#example 3
def string_builder (word1, word2, word3, word4):
    """This function returns the concatenation of the two words."""
    return f"{word1} {word2} {word3} {word4}"
new_random_variable = string_builder("hello", "2", "this", "is")
print(new_random_variable)