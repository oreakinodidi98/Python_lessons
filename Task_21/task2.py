# activate sqllite
import sqlite3
# using a try statment to create a database calle School, containing 2 tables
try:
     # Connect to the database. if it does not exist, it will be created. python cannot create a folder in the path. have to create the folder first
    database = sqlite3.connect("school") 
    # Create a cursor object to execute SQL queries and pull data from the database
    cursor = database.cursor()
    # Create a table called students and Course.
    #The Student table will have a foreign key to the Course table
    #The Course table contains the following attributes: course_code – a 5-character primary key; course_name – the name of the course; course_description – a description of the course; teacher_name – the name of the person who is teaching the course ;course_level – a number showing the level of the course (either 1, 2, or 3)
    cursor.execute("""CREATE TABLE IF NOT EXISTS Course (
                    course_code INTEGER PRIMARY KEY CHECK(length(course_code) = 5),
                    course_name TEXT NOT NULL,
                    course_description TEXT NOT NULL,
                    teacher_name  TEXT NOT NULL,
                    course_level INTEGER NOT NULL CHECK(course_level IN (1, 2, 3)))
                   """)
    cursor.execute("""CREATE TABLE IF NOT EXISTS Student (
                    student_id INTEGER PRIMARY KEY,
                    first_name VARCHAR(30) NOT NULL,
                   last_name VARCHAR(30) NOT NULL,
                    email VARCHAR(30) NOT NULL,
                    stu_subject_code CHAR(5) NOT NULL,
                    mark INTEGER NOT NULL,
                    FOREIGN KEY(stu_subject_code) REFERENCES Course(course_code))
                   """)
    # Commit the transaction
    database.commit()

    #list names and surnames of all students doing the DS03 cource
    cursor.execute("SELECT first_name, last_name FROM Student WHERE stu_subject_code = 'DS03'")
    # fetch all the results
    students = cursor.fetchall()
    # print the results
    for student in students:
        print(student)
        

except Exception as error_msg:
    # rollback any changes if an error occurs
    database.rollback()
    raise error_msg
# finally occurs no matter what
finally:
    # Close the connection
    database.close()