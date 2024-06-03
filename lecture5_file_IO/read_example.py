# example 1
# taking input from txt file and storing it in a variable called file
with open("jedis.txt", 'r') as file:
    content = file.read()
    print ("\nthis is the content of the file: \n")
    print (content)
    
# this will place the cursor at the beginning of the file
    file.seek(0)
    content = file.readline()
    print ("\nthis is the first line of the file \n")
    print (content)

    file.seek(0)
    content = file.readlines()
    print ("\nthis is the file in a list \n")
    print (content)

#example 2
with open("list_of_cats.txt", 'r') as file:
    for line in file:
        print (line, end='')
    file.seek(0)  # move the cursor back to the beginning of the file
    content = file.readline()  # read the first line
    print (f"\nthe first line of the file is: {content}")
    #print (content)

#example 3
    #example 2
with open("list_of_cats.txt", 'a') as file:
    user_input = input("Enter a cat name: ")
    file.seek(0)  # move the cursor back to the beginning of the file
    file.write(f"\n{user_input}")
    # define list of cats
    list_of_cats = ["Garfield", "Tom", "Sylvester", "Simba", "Nala", "Mufasa", "Bagheera", "Shere Khan", "Aslan", "Cheshire Cat"]
    # write the list of cats to the file in one line
    file.writelines(list_of_cats)
    # create another list of cats
    list_of_cats2 = ["Tigger", "Eeyore", "Piglet", "Roo", "Kanga", "Owl", "Rabbit", "Christopher Robin", "Pooh"]
    # write the list of cats to the file in a loop
    for cat in list_of_cats2:
        file.write(f"\n{cat}")

#example 4
# this will create the file named list_cats.txt
with open("list_cats.txt", 'w') as file:
    list_of_cats2 = ["Tigger", "Eeyore", "Piglet", "Roo", "Kanga", "Owl", "Rabbit", "Christopher Robin", "Pooh"]
    # write the list of cats to the file in a loop
    for cat in list_of_cats2:
        file.write(f"\n{cat}")
