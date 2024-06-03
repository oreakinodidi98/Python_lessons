class Student:

    def __init__(self, name, surname, age):
        self.name = name
        self.age = age
        self.surname = surname
    
    def __repr__(self) -> str:
        return f"{self.name} {self.surname} is {self.age} years old"
    
    def __str__(self) -> str:
        return f"Fullname:{self.name} {self.surname}\nAge: {self.age} years old"

student1 = Student("John", "Mc Ginn", 23)
student2 = Student("Jane", "Jones", 25)
str_student1 = str(student1)

print(student1)
print(type(student1))
print(student2)
print(str_student1)
print(type(str_student1))
