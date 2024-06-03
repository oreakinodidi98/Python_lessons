# define a function called random_number
def random_number():
    # import the random module
    import random
    # generate a random number between 1 and 100
    number = random.randint(1, 100)
    # return the random number
    return number
# test the function
print(random_number())