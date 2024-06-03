# activate sqllite
import sqlite3

# declare function to read the txt file
def txt_file(file_name):
    # Create an empty list to store the data
    student_data = []
    # Open and read the input file
    with open(file_name, "r") as file:
        # Iterate over each line in the file
        for line in file:
            # Split the line into fields using comma as delimiter
            fields = line.strip().split(',')
            # Convert student number to integer
            student_num = fields[0]
            # Extract other fields
            surname = fields[1]
            first_name = fields[2]
            initial = fields[3]
            start_date = fields[4]
            course_code = fields[5]
            proj_num = int(fields[6])
            # Append the data to the student_data list as a tuple
            student_data.append((student_num, surname, first_name, initial, 
                                 start_date, course_code, proj_num))
    return student_data
# using a try statment to create a database calle School, containing 2 tables
try:
     # Connect to the database. if it does not exist, it will be created. python cannot create a folder in the path. have to create the folder first
    database = sqlite3.connect("school") 
    # Create a cursor object to execute SQL queries and pull data from the database
    cursor = database.cursor()
    # Create a table called students
    cursor.execute("""CREATE TABLE IF NOT EXISTS Student (
                    STU_NUM CHAR(6) PRIMARY KEY,
                    STU_SNAME  VARCHAR(15) NOT NULL,
                    STU_FNAME VARCHAR(15) NOT NULL,
                   STU_INITIAL CHAR(1) NOT NULL,
                   STU_STARTDATE DATE NOT NULL,
                    COURSE_CODE CHAR(3) NOT NULL,
                   PROJ_NUM INT(2) NOT NULL )
                   """)
    # Commit the transaction
    database.commit()

    # different ways to insert data into the table
    #cursor.execute("INSERT OR REPLACE INTO Student(STU_NUM, STU_SNAME, STU_FNAME, STU_INITIAL, STU_STARTDATE, COURSE_CODE, PROJ_NUM) VALUES('01', 'Snow', 'Jon', 'E', '2014-04-05', '201', '6')")
    
    # can set values into a file to be read and inserted into the table
    student_data_= txt_file("student.txt")
    cursor.executemany("INSERT OR REPLACE INTO Student (STU_NUM,STU_SNAME,STU_FNAME,STU_INITIAL,STU_STARTDATE,COURSE_CODE,PROJ_NUM) VALUES (?,?,?,?,?,?,?)", student_data_)
    
    # can insert multiple values at once
    # cursor.executemany("""INSERT OR REPLACE INTO Student 
    #                       VALUES (?, ?, ?, ?, ?, ?, ?)""", 
    #                    [(2, 'Stark', 'Arya', 'C', '2017-07-12', '305', 11),
    #                     (3, 'Lannister', 'Jamie', 'L', '2012-09-05', '101', 2),
    #                     (4, 'Lannister', 'Cercei', 'J', '2012-09-05', '101', 2)])
    
    # Commit the transaction
    database.commit()
    
    # return all records which have course_code of 305
    course_code = 305
    cursor.execute("SELECT * FROM Student WHERE COURSE_CODE = ?", (course_code,))
    # display results
    print("********** Displaying course_code of 305 **********")
    #print(cursor.fetchall())
    for record in cursor:
        print(f"Student Number: {record[0]}, Student Surname: {record[1]}, Student First Name: {record[2]}")
        print(f"Student Initial: {record[3]}, Student Start Date: {record[4]}, Course Code: {record[5]}, Project Number: {record[6]}\n")

    # change course code to 304 for student number 07
    cursor.execute("UPDATE Student SET COURSE_CODE = '304' WHERE STU_NUM = '07'")
    # Commit the transaction
    database.commit()
    cursor.execute("SELECT * FROM Student")
    # display record to see if the course code is changed
    print("********** Displaying all records:change course code to 304 for student number 07 **********")
    for record in cursor:
        print(f"Student Number: {record[0]}, Student Surname: {record[1]}, Student First Name: {record[2]}")
        print(f"Student Initial: {record[3]}, Student Start Date: {record[4]}, Course Code: {record[5]}, Project Number: {record[6]}\n")

    # delete row of Jamie Lannister, started on 2012-09-05, course code 101, project number 2
    cursor.execute("DELETE FROM Student WHERE STU_SNAME = 'Lannister' AND STU_FNAME = 'Jamie' AND STU_STARTDATE = '2012-09-05' AND COURSE_CODE = '101' AND PROJ_NUM = '2'")
    # Commit the transaction
    database.commit()
    # display record to see if the record is deleted
    cursor.execute("SELECT * FROM Student")
    print("********** Displaying all records for deleted **********")
    for record in cursor:
        print(f"Student Number: {record[0]}, Student Surname: {record[1]}, Student First Name: {record[2]}")
        print(f"Student Initial: {record[3]}, Student Start Date: {record[4]}, Course Code: {record[5]}, Project Number: {record[6]}\n")

    #change PROJ_NUM to 14 for all students who started before 2016 and course code is at least 201
    cursor.execute("""UPDATE Student 
                      SET PROJ_NUM = 14 
                      WHERE STU_STARTDATE < '2016-01-01' AND COURSE_CODE >= '201'""")
    # Commit the transaction
    database.commit()
    # display all records
    cursor.execute("SELECT * FROM Student")
    print("********** Displaying all records to see updated **********")
    for record in cursor:
        print(f"Student Number: {record[0]}, Student Surname: {record[1]}, Student First Name: {record[2]}")
        print(f"Student Initial: {record[3]}, Student Start Date: {record[4]}, Course Code: {record[5]}, Project Number: {record[6]}\n")

    # delete student table
    cursor.execute("DROP TABLE Student")
    # Commit the transaction
    database.commit()
    # display record to see if the table is deleted
    cursor.execute("SELECT * FROM Student")
    print("********** Displaying all records **********")
    for record in cursor:
        print(f"Student Number: {record[0]}, Student Surname: {record[1]}, Student First Name: {record[2]}")
        print(f"Student Initial: {record[3]}, Student Start Date: {record[4]}, Course Code: {record[5]}, Project Number: {record[6]}\n")
    
except Exception as error_msg:
    # rollback any changes if an error occurs
    database.rollback()
    print(f"Error: {error_msg}")
    raise 
# finally occurs no matter what
finally:
    # Close the connection
    database.close()