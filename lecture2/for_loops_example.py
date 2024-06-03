#example 1
pokemon_list= ["pikachous","chazard","Squirtle","Gengar"]
for i in pokemon_list:
    print ("Current Pokemon:",i)

#example 2
random_set = "hello there General Ore"
for i in random_set:
    print ("Current letter:",i)

#example 3
for i in range(1, 10, 2):
    print ("Current number:",i)

#example 4
for i in range(1, 6):
    print ("Other number:",i)
# range(1,6) is the same as range(6) = [1,2,3,4,5]
    
#example 5
for i in range(1,4):
    print ("Outer loop position:",i)
    for j in range(1,4):
        print ("Inner loop position:",j)
        print ( i * j, end = " ")
        print("i * j:",i * j)
    print()

#example 6
random_set = "hello there General Ore"
random_set_split = random_set.split()
for i in random_set_split:
    print ("Current word:",i)
