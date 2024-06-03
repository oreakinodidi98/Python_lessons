# ask how many students are registering
input_students = input("How many students are registering? ")

# if input_students is not a number, the program will run a try and except block
try:
     # check if the input is a number
    if not input_students.isdigit():
        raise ValueError("Please only enter a whole number.")
    input_students = int(input_students)
except ValueError as e:
    print(e)
    exit()
    
# create for lop to register students
for i in range(input_students):
    # get user input
    student_name = input("Enter the student's name: ")
    student_id = input("Enter the student's ID: ")
    # if student_id is not a number, the program will run a try and except block
    try:
        # check if the input is a number
        if not student_id.isdigit():
            raise ValueError("Please only enter numbers.")
    except ValueError as e:
        print(e)
        exit()
    #write each of the ID number to a text file called reg_form.txt
    with open("reg_form.txt", 'a') as file:
        file.write(f"{student_name} {student_id}\n")
        # include a dotted line to separate each student's information
        file.write("-" * 30 + "\n")
    # print out the student's name and ID
    print(f"Student {student_name} with ID {student_id} has been registered.")