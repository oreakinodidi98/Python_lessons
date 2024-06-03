# task managment system
class Task:
    def __init__(self, task_id, title, description):
        # initialize the task object
        self.title = title
        self.description = description
        self.task_id = task_id
    
# CRUD Functions   
def display_tasks():
    # display the tasks information in a formatted way
    print(f"tasks information:")
    for task in task_data:
        print(f"\nTask ID: {task.task_id}, Title: {task.title}, Description: {task.description}")
        
def create_task(title, description):
    # add a new task to the task_data list
    # create new ID for the task
    new_id = len(task_data) + 1
    # create new task
    new_task = Task(new_id, title, description)
    task_data.append(new_task)
    print(f"\nTask {title} is added successfully!")

def read_task(task_id):
    # read and display task based of ID
    for task in task_data:
        if task.task_id == task_id:
            print(f"\nTask ID: {task.task_id}, Title: {task.title}, Description: {task.description}")
            return
        # if not found display message
    print(f"\nTask with ID {task_id} is not found!")

def update_task(task_id, title, description):
    # update task based on ID
    for task in task_data:
        if task.task_id == task_id:
            task.title = title
            task.description = description
            print(f"\nTask with ID {task_id} is updated successfully!")
            return
    # if not found display message
    print(f"\nTask with ID {task_id} is not found!")

def delete_task(task_id):
    # delete task based on ID
    for task in task_data:
        if task.task_id == task_id:
            task_data.remove(task)
            print(f"\nTask with ID {task_id} is deleted successfully!")
            return
    # if not found display message
    print(f"\nTask with ID {task_id} is not found!")

# sample data
# list of tasks, each task is an object of Task class
task_data = [Task(1, "Task 1", "This is task 1"),
            Task(2, "Task 2", "This is task 2"),
            Task(3, "Task 3", "This is task 3"),
            Task(4, "Task 4", "This is task 4")]

# display the tasks
display_tasks()
# create a new task
create_task("Task 5", "This is task 5")
# read a task
read_task(3)
# update a task
update_task(2, "Task 2 Updated", "This is task 2 updated")
# delete a task
delete_task(4)