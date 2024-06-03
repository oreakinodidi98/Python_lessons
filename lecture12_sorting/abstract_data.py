from queue import Queue

# creating a new queue
students = Queue()

# adding students to the queue
students.put("Alice")
students.put("Bob")
students.put("Charlie")

# iterating over all sstudents
while not students.empty():
    # get currrent student, remving them from the que 
    current_student = students.get()
    print(current_student)

# stacking
my_pets = []
#add 3 entries to the stack
my_pets.append("dog")
my_pets.append("cat")
my_pets.append("fish")
print(my_pets)
#remove the last element from the stack
my_pets.pop()
print(my_pets)

