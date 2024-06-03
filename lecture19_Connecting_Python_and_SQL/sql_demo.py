# Write the code to do the following tasks:
#
# - Create a table called employees.
# - Insert the following new rows into the employees table:

"""
  employ_num name     surname   department   position               level   salary 
    1001     Alice    Smith     HR           Manager                Senior  60000
    1002     Bob      Johnson   Engineering  Software Developer     Senior  75000
    1003     Charlie  Williams  Marketing    Marketing Coordinator  Mid     50000
    1004     David    Brown     Finance      Financial Analyst      Senior  65000
    1005     Emma     Jones     Sales        Sales Representative   Mid     55000
    1006     Frank    Miller    Engineering  Systems Engineer       Senior  80000
    1007     Grace    Davis     HR           HR Assistant           Junior  45000
    1008     Henry    Wilson    Finance      Accountant             Senior  70000
"""
# - Add a new employee: 1009,Isabella,Taylor,Marketing,Marketing Assistant,48000
# - Select all records with a salary between 45000 and 65000.
# - Change Emma Jones’ salary to 57000.
# - Delete Grace Davis' row.
# - Change the level to Junior for all people with a salary below 55000.

# create a txt file to put all information there

# activate sqllite

import sqlite3

# declare function to read the txt file
def read_file(file_name):
    # Create an empty list to store the data
    employees_data = []
    # Open and read the input file
    with open(file_name, "r") as file:
        # Iterate over each line in the file
        for line in file:
            # Split the line into fields using comma as delimiter
            fields = line.strip().split(',')
            # Convert employee number to integer
            employee_id = int(fields[0])
            # Extract other fields
            name = fields[1]
            surname = fields[2]
            department = fields[3]
            position = fields[4]
            level = fields[5]
            # Convert salary to float
            salary = float(fields[6])
            # Append the data to the employees_data list as a tuple
            employees_data.append((employee_id, name, surname, department, 
                                   position, level, salary))

    return employees_data

# try statment to create the database
try:
    # Connect to the database. if it does not exist, it will be created. python cannot create a folder in the path. have to create the folder first
    db = sqlite3.connect("employees_db") # or connect('data/employees_db.db')
    # Create a cursor object to execute SQL queries and pull data from the database
    cursor = db.cursor()
    # Create a table called employees. giving column names and data types
    cursor.execute("""CREATE TABLE IF NOT EXISTS employees (
                    employ_id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    surname TEXT NOT NULL,
                    department TEXT NOT NULL,
                    position TEXT NOT NULL,
                    level TEXT NOT NULL,
                    salary REAL)""")
    # Commit the transaction
    db.commit()

    # call the function to read the file
    employees_data_ = read_file("sqldemo.txt")
    # underscore at the end of the variable name is used to avoid conflict with the built-in function

    # Insert or replace the data into the employees table
    cursor.executemany("INSERT OR REPLACE INTO employees (employ_id,name,surname,department,position,level,salary) VALUES (?,?,?,?,?,?,?)", employees_data_)

    # add a new emploee
    new_employee = (1010, 'Isabella', 'Taylor', 'Marketing', 'Marketing Assistant', 'Junior', 48000)
    # Insert the new employee into the employees table
    cursor.execute("INSERT OR REPLACE INTO employees (employ_id,name,surname,department,position,level,salary) VALUES (?,?,?,?,?,?,?)", new_employee)
    # Commit the transaction
    db.commit()
    # display record to see if the new employee is added
    print("********** Displaying all records **********")
    cursor.execute("SELECT * FROM employees")
    for record in cursor.fetchall():
        #print(record)
        # or print each row in 2 lines with labels using f string
        print(f"Employee ID: {record[0]}, Name: {record[1]}, Surname: {record[2]}")
        print(f"Department: {record[3]}, Position: {record[4]}, Level: {record[5]}, Salary: {record[6]}\n")

    # Select all records with a salary between 45000 and 65000
    cursor.execute("SELECT * FROM employees WHERE salary BETWEEN 45000 AND 65000")
    # can also write as:
    # cursor.execute("SELECT * FROM employees WHERE salary BETWEEN ? AND ?", (45000, 65000))
    #start_range = 45000
    #end_range = 65000
    #cursor.execute("SELECT * FROM employees WHERE salary BETWEEN ? AND ?", (start_range, end_range))
    # Display the records with salary between 45000 and 65000
    print("********** Displaying records with salary between 45000 and 65000 **********")
    for record in cursor:
        print(f"Employee ID: {record[0]}, Name: {record[1]}, Surname: {record[2]}")
        print(f"Department: {record[3]}, Position: {record[4]}, Level: {record[5]}, Salary: {record[6]}\n")

    # Change Emma Jones’ salary to 57000
    cursor.execute("UPDATE employees SET salary = 57000 WHERE name = 'Emma' AND surname = 'Jones'")
    # can also write as:
    # cursor.execute("UPDATE employees SET salary = ? WHERE name = ? AND surname = ?", (57000, 'Emma', 'Jones'))
    #name = 'Emma'
    #surname = 'Jones'
    #new_salary = 57000
    #cursor.execute("UPDATE employees SET salary = ? WHERE name = ? AND surname = ?", (new_salary, name, surname))
    # Commit the transaction
    db.commit()
    # Display the updated record
    cursor.execute("SELECT * FROM employees WHERE name = 'Emma' AND surname = 'Jones'")
    # Display the record with updated salary
    print("********** Displaying the record of Emma Jones with updated salary **********")
    # can also use fetchone() to get only one record
    # record = cursor.fetchone()
    # print(f"Employee ID: {record[0]}, Name: {record[1]}, Surname: {record[2]}")
    for record in cursor:
        print(f"Employee ID: {record[0]}, Name: {record[1]}, Surname: {record[2]}")
        print(f"Department: {record[3]}, Position: {record[4]}, Level: {record[5]}, Salary: {record[6]}\n")
    
    # Delete Grace Davis' row
    cursor.execute("DELETE FROM employees WHERE name = 'Grace' AND surname = 'Davis'")
    # Commit the transaction
    db.commit()
    # Display the updated record to see if Grace Davis' row is deleted
    cursor.execute("SELECT * FROM employees")
    # display record to see if the new employee is added
    print("********** Displaying all records with deleted GRACE davis **********")
    cursor.execute("SELECT * FROM employees")
    for record in cursor:
        print(f"Employee ID: {record[0]}, Name: {record[1]}, Surname: {record[2]}")
        print(f"Department: {record[3]}, Position: {record[4]}, Level: {record[5]}, Salary: {record[6]}\n")
    
    # can also use an if statment to check is cursor is empty before deleting

    # if not cursor.fetchall()
    #     print("No records found")
    # else:
    #     cursor.execute("DELETE FROM employees WHERE name = 'Grace' AND surname = 'Davis'")
    #     db.commit()


    # Change the level to Junior for all people with a salary below 55000
    cursor.execute("UPDATE employees SET level = 'Junior' WHERE salary < 55000")
    # can also write as:
    # cursor.execute("UPDATE employees SET level = ? WHERE salary < ?", ('Junior', 55000))
    # Commit the transaction
    db.commit()
    # Display the updated records
    cursor.execute("SELECT * FROM employees")
    # Display the records with updated level
    print("********** Displaying records with updated level **********")
    for record in cursor:
        print(f"Employee ID: {record[0]}, Name: {record[1]}, Surname: {record[2]}")
        print(f"Department: {record[3]}, Position: {record[4]}, Level: {record[5]}, Salary: {record[6]}\n")

except Exception as error_msg:
    # rollback any changes if an error occurs
    db.rollback()
    raise error_msg
# finally occurs no matter what
finally:
    # Close the connection
    db.close()