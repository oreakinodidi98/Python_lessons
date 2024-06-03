import os
# example 1
# taking input from txt file and storing it in a variable called file
with open("jedis.txt", 'r') as file:
    content = file.readlines()
    print (content)
    file.close()

# read()
    # returns the file content as a string
# readline()
    # returns the first line of the file
# readlines()
    # returns a list of all the lines in the file

# example 2
# writing to a file
# this will overwrite the file
with open("jedis.txt", 'w') as file:
    file.write("Yoda\n")
    file.write("Obi Wan Kenobi\n")
    file.write("Luke Skywalker\n")
    file.write("Mace Windu\n")
    file.write("Qui-Gon Jinn\n")
    file.write("Anakin Skywalker\n")
    file.write("Rey\n")
    file.write("Ahsoka Tano\n")
    file.write("Ki-Adi-Mundi\n")

# example 3
# appending to a file
# this will add to the file
with open("jedis.txt", 'a') as file:
    file.write("Darth Vader\n")
    file.write("Darth Sidious\n")
    file.write("Darth Maul\n")
    file.write("Kylo Ren\n")
    file.write("Count Dooku\n")
    file.write("Asajj Ventress\n")
    file.write("Savage Opress\n")
    file.write("General Grievous\n")
    file.write("Barriss Offee\n")

# example 4
# Append - creates the file if it doesnt exisst
f = open("jedis.txt", 'a')
f.write("Aayla Secura\n")
f.close()

f = open("jedis.txt")
print(f.read())
f.close()

# example 5
#write (overwite)
f = open("list_of_cats.txt", 'w')
f.write("I deleted all of the context\n")
f.close()

f = open("list_of_cats.txt")
print(f.read())
f.close()

# ways to create a new file 

# oens a file for writting, creates the file if it does not exisst
f= open("list_of_name.txt", 'w')
f.close()

# creates the specified file but returns an error if the file exists
#check to see if a file name exists
if not os.path.exists("list_of_name.txt"):
    f = open("list_of_name.txt", 'x')
    f.close()

# delete a file
# can avoid an error if it doesnt exist
if os.path.exists("list_of_name.txt"):
    os.remove("list_of_name.txt")
else:
    print("The file you wish to delete does not exist")

with open("jedis.txt") as f:
    content = f.read()

with open("more_jedis.txt", 'w') as f:
    f.write(content)
