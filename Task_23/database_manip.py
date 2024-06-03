# activate sqllite
import sqlite3

# using a try statment to create a database calle School, containing 2 tables
try:
     # Connect to the database. if it does not exist, it will be created. python cannot create a folder in the path. have to create the folder first
    database = sqlite3.connect("task23") 
    # Create a cursor object to execute SQL queries and pull data from the database
    cursor = database.cursor()
    # Create a table called students
    cursor.execute("""CREATE TABLE IF NOT EXISTS python_programming (
                    ID INT(1) PRIMARY KEY,
                    NAME  VARCHAR(20) NOT NULL,
                    GRADE INT(2) NOT NULL )
                   """)
    # Commit the transaction
    database.commit()
    # list of tuples to be inserted into the table
    database_values = [(55, 'Carl Davis', 61), 
                       (66, 'Dennis Fredrickson', 88), 
                       (77, 'Jane Richards ', 78), 
                       (12, 'Peyton Sawyer', 45), 
                       (2, 'Lucas Brooke ', 99)]
    #insert into table
    cursor.executemany("INSERT OR REPLACE INTO python_programming (ID, NAME, GRADE) VALUES (?,?,?)", database_values)
    # Commit the transaction
    database.commit()
    # get id
    id = cursor.lastrowid
    print('Last row id: %d' % id)
    #get all items in the table
    cursor.execute("SELECT * FROM python_programming")
    # display results
    print("********** Displaying all records **********")
    for record in cursor:
        print(f"ID: {record[0]}, Name: {record[1]}, Grade: {record[2]}")
    
    #  select all students with grade between 60 and 80
    cursor.execute("SELECT * FROM python_programming WHERE GRADE BETWEEN 60 AND 80")
    # display results
    print("********** Displaying students with grade between 60 and 80 **********")
    for record in cursor:
        print(f"ID: {record[0]}, Name: {record[1]}, Grade: {record[2]}")

    # Change Carl Davis grade to 65
    cursor.execute("UPDATE python_programming SET GRADE = 65 WHERE NAME = 'Carl Davis'")
    # Commit the transaction
    database.commit()
    cursor.execute("SELECT * FROM python_programming")
    # display record to see if the grade is changed
    print("********** Displaying all records: change Carl Davis grade to 65 **********")
    for record in cursor:
        print(f"ID: {record[0]}, Name: {record[1]}, Grade: {record[2]}")

    # delete row of Dennis Fredrickson
    cursor.execute("DELETE FROM python_programming WHERE NAME = 'Dennis Fredrickson'")
    # Commit the transaction
    database.commit()
    cursor.execute("SELECT * FROM python_programming")
    # display record to see if the row is deleted
    print("********** Displaying all records: delete Dennis Fredrickson **********")
    for record in cursor:
        print(f"ID: {record[0]}, Name: {record[1]}, Grade: {record[2]}")

    # Change grade of students with an id greater than 55 to 80
    cursor.execute("UPDATE python_programming SET GRADE = 80 WHERE ID > 55")
    # Commit the transaction
    database.commit()
    cursor.execute("SELECT * FROM python_programming")
    # display record to see if the grade is changed
    print("********** Displaying all records: change grade of students with an id greater than 55 to 80 **********")
    for record in cursor:
        print(f"ID: {record[0]}, Name: {record[1]}, Grade: {record[2]}")
        
except Exception as error_msg:
    # rollback any changes if an error occurs
    database.rollback()
    print(f"Error: {error_msg}")
    raise 
# finally occurs no matter what
finally:
    # Close the connection
    database.close()