"""
Task: 
------------------
1. Add another method in the Course class that prints the head office location: Cape Town
2. Create a subclass of the Course class named OOPCourse
3. Create a constructor that initialises the following attributes and assigns these values:
    --- "description" with a value "OOP Fundamentals"
    --- "trainer" with a value "Mr Anon A. Mouse"
4. Create a method in the subclass named "trainer_details" that prints what the 
   course is about and the name of the trainer by using the description and trainer attributes.
5. Create a method in the subclass named "show_course_id" that prints the ID number of the course: #12345
6. Create an object of the subclass called course_1 and call the following methods
   contact_details
   trainer_details
   show_course_id
   These methods should all print out the correct information to the terminal

Note: this task covers single inheritance. Multiple inheritance is also possible in Python and 
we encourage you to do some research on multiple inheritance when you have finished this course.
"""
class Course:
    name = "Fundamentals of Computer Science"
    contact_website = "www.hyperiondev.com"
    location = "Cape Town"

    def contact_details(self):
        print("Please contact us by visiting", self.contact_website)

    # method to print head office location
    def head_office(self):
        print(f"Head office location:{self.location}")

# create subclass of Course named OOPCourse
class OOPCourse(Course):
    # constructor to initialise attributes with default values
    def __init__(self):
        self.description = "OOP Fundamentals"
        self.trainer = "Mr Anon A. Mouse"

    # method to print course description and trainer name
    def trainer_details(self):
        print(f"Course description: {self.description}\nTrainer: {self.trainer}")

    # method to print course ID
    def show_course_id(self):
        print("Course ID: #12345")

# object of the OOPCourse subclass called course_1
course_1 = OOPCourse()
#call contact_details method
course_1.contact_details()
# call trainer_details method
course_1.trainer_details()
# call show_course_id method
course_1.show_course_id()