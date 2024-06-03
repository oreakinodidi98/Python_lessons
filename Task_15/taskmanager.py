from datetime import datetime
# assighed datetime to a variable called current_dateTime
current_dateTime = datetime.now()

class Filelibrary:
    def __init__(self, file_id, file_title, description, folder_id, priority, status, created_at, updated_at):
        # initialize the task object
        self.file_title = file_title
        self.description = description
        self.file_id = file_id
        self.folder_id = folder_id
        self.priority = priority
        self.status = status
        self.created_at = created_at
        self.updated_at = updated_at

# Display all current files
def display_files():
    # display the files information in a formatted way
    print(f"Current Files:")
    for file in file_data:
        print(f"\nFile ID: {file.file_id}, Title: {file.file_title}, Description: {file.description}, Folder ID: {file.folder_id}, Priority: {file.priority}, Status: {file.status}, Created At: {file.created_at}, Updated At: {file.updated_at}")

# Create new file function
def create_file(file_title, description, priority, status):
    # add a new file to the file_data list
    # create new ID for the file
    new_id = len(file_data) + 2
    new_folder_id = len(file_data) + 2
    # create new file
    new_file = Filelibrary(new_id, file_title, description, new_folder_id, priority, status, current_dateTime, current_dateTime)
    file_data.append(new_file)
    print(f"\nFile {file_title} is added successfully!")

# Read specific file function based of file_id
def serch_file (file_id):
    # read and display file based of ID
    for file in file_data:
        if file.file_id == file_id:
            print(f"\nFile ID: {file.file_id}, Title: {file.file_title}, Description: {file.description}, Folder ID: {file.folder_id}, Priority: {file.priority}, Status: {file.status}, Created At: {file.created_at}, Updated At: {file.updated_at}")
            return
        # if not found display message
    print(f"\nFile with ID {file_id} is not found!")

# Update file function based on file_id
def update_file (file_id, file_title, description, priority, status):
    # update file based on ID
    for file in file_data:
        if file.file_id == file_id:
            file.file_title = file_title
            file.description = description
            file.priority = priority
            file.status = status
            file.updated_at = current_dateTime
            print(f"\nFile with ID {file_id} is updated successfully!")
            print(f"\nNew file information is:\nFile ID: {file.file_id}, Title: {file.file_title}, Description: {file.description}, Folder ID: {file.folder_id}, Priority: {file.priority}, Status: {file.status}, Created At: {file.created_at}, Updated At: {file.updated_at}")
            return
    # if not found display message
    print(f"\nFile with ID {file_id} is not found!")

# Delete file function based on file_id
def delete_file (file_id):
    # delete file based on ID
    for file in file_data:
        if file.file_id == file_id:
            file_data.remove(file)
            print(f"\nFile with ID {file_id} is deleted successfully!")
            return
    # if not found display message
    print(f"\nFile with ID {file_id} is not found!")


# sample data, list of files, each file is an object of filelibray class
file_data = [Filelibrary(1, "File 1", "This is file 1", 1, "High", "Active", "2021-01-01", "2021-01-01"),
                Filelibrary(2, "File 2", "This is file 2", 2, "Medium", "Active", "2021-01-01", "2021-01-01"),
                Filelibrary(3, "File 3", "This is file 3", 3, "Low", "Active", "2021-01-01", "2021-01-01"),
                Filelibrary(4, "File 4", "This is file 4", 4, "High", "Active", "2021-01-01", "2021-01-01")]

# display the files
display_files()
#update a file
update_file(2, "File 2 Updated", "This is file 2 updated", "Low", "Inactive")
#delete a file
delete_file(3)
display_files()
# create a new file
create_file("File 5", "This is file 5", "High", "Active" )
display_files()

#  logic for the menu operations.

while True:
    user_choice = int(input('''\nWould you like to:
    1. Display All Files
    2. Update File
    3. Delete File
    4. Search For File
    5. Create File
    6. Quit application

    Enter selection: '''))
       
    if user_choice == 1:
    # add logic to Display All Files
         display_files()
    elif user_choice == 2:
        # add logic here to Update specific File
        file_id = input("\nEnter the ID of the file you want to update:")
        # if file_id input is not a nummber, the program will run a try and except block
        try:
            # check if the input is a number
            if not file_id.isdigit():
                raise ValueError("Please only enter numbers.")
            file_id = int(file_id)
        except ValueError as e:
            print(e)
            exit()
        file_title = input("\nEnter the new title of the file:")
        description = input("\nEnter the new description of the file:")
        priority = input("\nEnter the new priority of the file (high, medium, low):")
        # try and except block to check if the input is one of the priority levels high, medium or low
        try:
            if priority.lower() not in ["high", "medium", "low"]:
                raise ValueError("Please only enter high, medium or low.")
            priority = str(priority)
        except ValueError as e:
            print(e)
            exit()
        status = input("\nEnter the new status of the file (active or inactive):")
        # try and except block to check if the input is one of the status levels active or inactive
        try:
            if status.lower() not in ["active", "inactive"]:
                raise ValueError("Please only enter active or inactive.")
            status = str(status)
        except ValueError as e:
            print(e)
            exit()
        update_file(file_id, file_title, description, priority, status)
    elif user_choice == 3:
        # add logic here to delete specific File
        file_id = int(input("\nEnter the ID of the file you want to delete:"))
        delete_file(file_id)
    elif user_choice == 4:
        # add logic here to search for specific File
        file_id = int(input("\nEnter the ID of the file you want to search for:"))
        serch_file(file_id)
    elif user_choice == 5:
        # add logic here to create new File
        file_title = input("\nEnter the title of the file:")
        description = input("\nEnter the description of the file:")
        priority = input("\nEnter the priority of the file (high, medium, low):")
        # try and except block to check if the input is one of the priority levels high, medium or low
        try:
            if priority.lower() not in ["high", "medium", "low"]:
                raise ValueError("Please only enter high, medium or low.")
            priority = str(priority)
        except ValueError as e:
            print(e)
            exit()
        status = input("\nEnter the status of the file (active or inactive):")
        # try and except block to check if the input is one of the status levels active or inactive
        try:
            if status.lower() not in ["active", "inactive"]:
                raise ValueError("Please only enter active or inactive.")
            status = str(status)
        except ValueError as e:
            print(e)
            exit()
        create_file(file_title, description, priority, status, current_dateTime, current_dateTime.day)
    elif user_choice == 6:
        print("Goodbye!")
        break
    else:
        print("Oops - incorrect input.")