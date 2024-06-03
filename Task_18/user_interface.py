from buisness_logic import TaskManager

def start_application():
    # Start the Task Management Application.
    # Create an instance of the TaskManager class
    task_manager = TaskManager()

    while True:
        user_choice = int(input('''\nWould you like to:
        1. Display All Tasks
        2. Update Task
        3. Delete Task
        4. Search For Specific Task
        5. Create Task
        6. Quit application

        Enter selection: '''))
        
        if user_choice == 1:
        # add logic to Display All tasks
            tasks = task_manager.get_all_tasks()
            print(f"\n{tasks}")
        
        elif user_choice == 2:
            # add logic here to Update specific File
            while True:
                file_id = input("\nEnter the ID of the task you want to update:")
                # if file_id input is not a nummber, the program will run a try and except block
                try:
                    # check if the input is a number
                    if not file_id.isdigit():
                        raise ValueError("Please only enter numbers.")
                    file_id = int(file_id)
                    break
                except ValueError as e:
                    print(e)
                    continue # continue the loop if the input is incorrect
            while True:
                file_title = input("\nEnter the new title of the task:")
                if file_title.strip():  # Check if title is not empty
                    break
                else:
                    print("Title cannot be empty. Please try again.")
            while True:
                description = input("\nEnter the new description of the task:")
                if description.strip():  # Check if description is not empty
                    break
                else:
                    print("Description cannot be empty. Please try again.")
            while True:
                priority = input("\nEnter the new priority of the file (high, medium, low):")
                # try and except block to check if the input is one of the priority levels high, medium or low
                try:
                    if priority.lower() not in ["high", "medium", "low"]:
                        # raise an error if the input is not one of the priority levels high, medium or low
                        raise ValueError("Please only enter high, medium or low.")
                    # set the priority to a string
                    priority = str(priority)
                    break
                    # except block to catch the error
                except ValueError as e:
                    # print the error message
                    print(e)
                    continue
            while True:    
                status = input("\nEnter the new status of the file (active or inactive):")
                # try and except block to check if the input is one of the status levels active or inactive
                try:
                    if status.lower() not in ["active", "inactive"]:
                        raise ValueError("Please only enter active or inactive.")
                    status = str(status)
                    break
                except ValueError as e:
                    print(e)
                    continue # continue the loop if the input is incorrect
            
            tasks = task_manager.update_current_task(file_id, file_title, description, priority, status)
            print(f"\n{tasks}")
        
        elif user_choice == 3:
            # add logic here to delete specific File
            while True:
                file_id = input("\nEnter the ID of the task you want to delete:")
                # if file_id input is not a nummber, the program will run a try and except block
                try:
                    # check if the input is a number
                    if not file_id.isdigit():
                        raise ValueError("Please only enter numbers.")
                    file_id = int(file_id)
                    break
                except ValueError as e:
                    print(e)
                    continue # continue the loop if the input is incorrect
            tasks = task_manager.delete_current_task(file_id)
            print(f"\n{tasks}")
        
        elif user_choice == 4:
            # add logic here to search for specific File
            while True:
                file_id = input("\nEnter the ID of the task you want to search for:")
                # if file_id input is not a nummber, the program will run a try and except block
                try:
                    # check if the input is a number
                    if not file_id.isdigit():
                        raise ValueError("Please only enter numbers.")
                    file_id = int(file_id)
                    break
                except ValueError as e:
                    print(e)
                    continue # continue the loop if the input is incorrect
            # search for the file
            tasks = task_manager.search_current_task(file_id)
            # print the function output
            print(f"\n{tasks}")
        
        elif user_choice == 5:
            # add logic here to create new File
            # Loop for title input
            while True:
                file_title = input("\nEnter the title of the new task:")
                if file_title.strip():  # Check if title is not empty
                    break
                else:
                    print("Title cannot be empty. Please try again.")
            # Loop for description input
            while True:
                description = input("\nEnter the description of the task:")
                if description.strip():  # Check if description is not empty
                    break
                else:
                    print("Description cannot be empty. Please try again.")
            # Loop for priority input
            while True:
                priority = input("\nEnter the priority of the task (high, medium, low):")
                # try and except block to check if the input is one of the priority levels high, medium or low
                try:
                    if priority.lower() not in ["high", "medium", "low"]:
                        raise ValueError("Please only enter high, medium or low.")
                    priority = str(priority)
                    break
                except ValueError as e:
                    print(e)
                    continue # continue the loop if the input is incorrect
            # Loop for status input
            while True:
                status = input("\nEnter the status of the file (active or inactive):")
                # try and except block to check if the input is one of the status levels active or inactive
                try:
                    if status.lower() not in ["active", "inactive"]:
                        raise ValueError("Please only enter active or inactive.")
                    status = str(status)
                    break
                except ValueError as e:
                    print(e)
                    continue # continue the loop if the input is incorrect
            # save the new task
            tasks = task_manager.save_current_task(None, file_title, description, priority, status)
            # print the file
            print(f"\n{tasks}")
        
        elif user_choice == 6:
            print("Goodbye!")
            break
        else:
            print("Oops - incorrect input.")