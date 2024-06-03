# input string
string = input("Enter a string: ")
#alternate characters of the string into an uppercase character and lowercase character
# when a user enters any input that is not a string, the program will run a try and except block
try:
    # check if the input is a string (allowing spaces)
    if not string.replace(" ", "").isalpha():
        raise ValueError("Please only enter a valid string.")
except ValueError as e:
    print(e)
    exit()

# define a new string
new_string = ""

# loop through the string input
for i in range(len(string)):
    # check if the index is even or odd
    if i % 2 == 0:
        # if even, convert to uppercase
        new_string += string[i].upper()
    else:
        # if odd, convert to lowercase
        new_string += string[i].lower()

# print the new string
print(f"Task 1: {new_string}")

# Split the input string into words
words = string.split()
# define a new string variable for alternative characters
new_string_alt = ""
# Define a new list for the modified words
new_words = []

# make each alternative word lower and upper case
for i in range(len(words)):
    if i % 2 == 0:
        # If even, convert the word to uppercase and append to the new list
        new_words.append(words[i].upper())
    else:
        # If odd, convert the word to lowercase and append to the new list
        new_words.append(words[i].lower())

# Join the modified words into a single string
new_string_alt = " ".join(new_words)
# print the new string
print(f"Task 2: {new_string_alt}")