# setting up python projects

- good idea to set upp virtual enviroments and a requirements.txt file and installing a linter
- allows you to create isolated environments for your projects, each with its dependencies, without affecting the system-wide Python installation, supporting your development workflow
- Remember to activate the virtual environment whenever you work on your project, to ensure that the dependencies you install are specific to your project and don't interfere with other projects or the system-wide Python installation#

## Virtual enviroments

- isolate project dependencies and avoid conflicts

## file structure

- src
  - module1
    - __init__.py
    - module1.py
  - module2
    - __init__.py
    - module2.py
- test
  - test module1
  - test module2
- readme
- requirments.txt
- .gitignore

## dependencyy managment

- Creating a requirements.txt file is a common practice in Python development to document and manage project dependencies
- lists all the Python packages and their versions that your project depends on, making it easier forothers to replicate your environment
- pip freeze > requirements.txt

## version control

- git init

## linting

- help enforce coding standards and identify potential issues early in development
- Popular Python linters include **Flake8** and **pylint**
- Linting is a process of analysing code for potential errors, style violations, and other issues.
- It helps maintain a consistent and high-quality codebase
- We use a Python linter called Flake8

```powershell
C:\codebootcamp\lecture1> flake8 lecture14_Unit_Testing/example2.py
```

## defining modules tp seperate concerns

- a module is a file containing Python definitions and statements
- file name is the module name with the suffix .py added.
- allow you to organise your code into separate files, making it easier to manage and understand. They also enable code reuse and maintainability.
- good file structure:
- my project/
- main.py
- data_access.py
- buisness_logic.py
- user_interface.py
- utilities.py
- config.py
- tests/
  - tests.py
- constants.py

```py
#main.py
from user_interface import start_application

if __name__ == "__main__":
    start_application()
```

- This is the main entry point of the application.
- It imports the start_application function from the user_interface module.
- The __name__ == "__main__" condition ensures that the start_application function is called only when the script is executed directly, not when it is imported as a module

```py
#data_access.py
class TaskRepository:
    def get_tasks(self):
        """ Retrieve tasks from the data source"""
    # placeholder implementation - replace with actual data retriieval logic 
    pass

    def save_task (self, task)
    """save a task to the data sink"""
    pass
```

- repository pattern
- The repository pattern is a design pattern commonly used in software development to separate the logic that retrieves data from the underlying storage system (such as a database) from the rest of the application
- This module defines a TaskRepository class responsible for handling data access operations
- It includes methods get_tasks and save_task for retrieving tasks from, and saving tasks to, a data source, respectively.

```py
# business_logic.py
from data_access import TaskRepository

class TaskService:
    def __init__(self):
        """ Initialise the TaskService with a TaskRepository."""
    self.task_repository = TaskRepository()

    def get_all_tasks(self):
    """ Get all tasks from the data source."""
    return self.task_repository.get_tasks()

    def add_task(self, task):
    """ Add a new task to the data source."""
    self.task_repository.save_task(task)

```

- This module defines a TaskService class that encapsulates the business logic of the application.
- (A service is called a "service" because it provides a service or a well-defined set of operations that can be utilised by other parts of the application.)
- It initialises a TaskRepository in the constructor to interact with the data source.
- The methods get_all_tasks and add_task use the TaskRepository to get all tasks, and add a new task, respectively

```py
# user_interface.py
from business_logic import TaskService

def start_application():
    """ Start the Task Management Application."""
    task_service = TaskService()

    while True:
    print("Task Management Application")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        tasks = task_service.get_all_tasks()
        print("Tasks:")
        for task in tasks:
            print(f"- {task}")
    elif choice == "2":
        new_task = input("Enter task description: ")
        task_service.add_task(new_task)
        print("Task added successfully!")
    elif choice == "3":
        print("Exiting the application. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again")

```

- This module contains the user interface logic for the application.
- The start_application function initialises a TaskService.
- It provides a simple command-line interface for users to view tasks, add tasks, or quit the application.
- The user's input determines the action to be taken, and the corresponding methods of TaskService are called.

```py
# utilities.py
def format_date(date):
    """ Format a date string."""
    pass
```

- This module defines a utility function, format_date, for formatting date strings.
- The function can be used across the application for consistent date formatting.

```py
# config.py
FILENAME = "data.txt"
```

- This module holds configuration settings for the application.
- FILENAME is an example configuration parameter representing the filename for the file we will back our data to.
- In a real-world scenario, this module could contain a variety of configuration settings for a database connection. For the scope of this task, we will focus on the filename

```py
# tests.py
import unittest
from business_logic import TaskService, Task

class TestTaskService(unittest.TestCase):
    def test_add_task(self):
        """Test the add_task method of TaskService."""
        # Arrange
        task_service = TaskService()
        initial_task_count = len(task_service.get_all_tasks()) 
        # Get initial task count
        new_task = Task(title="New Task", description="Description of
        the new task")
        
        # Act
        task_service.add_task(new_task)
        
        # Assert
        updated_task_count = len(task_service.get_all_tasks()) 
        # Get updated task count
        self.assertEqual(updated_task_count, initial_task_count + 1) 
        # Check if the task count increased by 1
        self.assertIn(new_task, task_service.get_all_tasks()) 
        # Check if the new task is in the list of tasks

if __name__ == "__main__":
    unittest.main()
```

- **Arrange**: Set up the necessary objects and conditions for the test. 
- In this case, create an instance of TaskService, get the initial task count, and create a new task.
- **Act**: Perform the action you are testing. In this case, call the add_task method with the new task.
- **Assert**: Check whether the actual result matches the expected result.
- Here, we check whether the task count has increased by one and whether the new task is in the list of tasks.

```py
# constants.py
TASK_MAX_LENGTH = 100
```

- This module defines constant values that can be used across the application.
- TASK_MAX_LENGTH is an example constant representing the maximum length allowed for a task description.

## create a Virtual enviroment

```py
python -m venv venv
or 
python3 -m venv venv
```

- activate the virtual enviroment: venv\Scripts\activate.bat
- or : . .\venv\Scripts\Activate
- install dependencies: pip install django
- Deactivate the virtual environment: venv\Scripts\deactivate.bat
- or : deactivate

## generating a requirements file

- document outlining the specific Python packages and their corresponding versions required for the project to run successfully.
- you can use the pip freeze command
- This command lists all installed packages and their versions.
- Here's how you can create a requirements.txt
- activate virtual nviroment: . .\venv\Scripts\Activate
- run command: pip freeze > requirements.txt
  - This command creates a requirements.txt file containing the names and versions of all installed packages
  - to include only the packages needed for your project (excluding development dependencies), you can use the:
  - pip freeze --exclude-editable > requirements.txt