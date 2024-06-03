# function called capital_indexes
def capital_indexes(string):
    # create a list called indexes
    indexes = []
    # create a for loop to iterate through the string
    for i in range(len(string)):
        # if the character is an uppercase letter, append the index to the indexes list
        if string[i].isupper():
            indexes.append(i)
    # return the indexes list
    return indexes
# test the function
print(capital_indexes("HeLLo")) # [0, 2, 3]