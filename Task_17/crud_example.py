# task managment system
class Task:
    # class to manage tasks

    # list to store tasks
    task_data = []

    # create constructor with 3 parameters
    def __init__(self, task_id, title, description):
        # initialize the task object
        self.title = title
        self.description = description
        self.task_id = task_id
        
    #method to display tasks in the list  
    def display_tasks(self):
        # display the tasks information in a formatted way
        tasks_info = ""
        for task in self.task_data:
            tasks_info += f"\nTask ID: {task.task_id}, Title: {task.title}, Description: {task.description}"
        return tasks_info
    
    #method to read a task based on ID
    def read_task(self,task_id):
        # read and display task based of ID
        for task in self.task_data:
            # if found display task information
            if task.task_id == task_id:
                return f"\nTask ID: {task.task_id}, Title: {task.title}, Description: {task.description}"
            # if not found display message
        return f"\nTask with ID {task_id} is not found!"

    #method to create a new task      
    def create_task(self, title, description):
        # add a new task to the task_data list & create new ID for the task
        new_id = len(self.task_data) + 1
        # check if iD is already in the list
        for task in self.task_data:
            if task.task_id == new_id:
                new_id += 1
        # create new task
        new_task = Task(new_id, title, description)
        # add the new task to the list
        self.task_data.append(new_task)
        return f"\n{title} is added successfully!"


    def update_task(self, task_id, title, description):
        # update task based on ID
        for task in self.task_data:
            if task.task_id == task_id:
                task.title = title
                task.description = description
                return f"\nTask with ID {task_id} is updated successfully!"
                # if not found display message
        return f"\nTask with ID {task_id} is not found!"
        
    def delete_task(self, task_id):
        # delete task based on ID
        for task in self.task_data:
            if task.task_id == task_id:
                self.task_data.remove(task)
                return f"\nTask with ID {task_id} is deleted successfully!"
        # if not found display message
        return f"\nTask with ID {task_id} is not found!"



# Create an instance of TaskManager
task_manager = Task(1, "Task 1", "This is task 1")
# Add tasks to the task_manager
task_manager.task_data = [Task(1, "Task 1", "This is task 1"),
                          Task(2, "Task 2", "This is task 2"),
                          Task(3, "Task 3", "This is task 3"),
                          Task(4, "Task 4", "This is task 4")]
# display the tasks
print(task_manager.display_tasks())
# create a new task
print(task_manager.create_task("Task 5", "This is task 5"))
# read a task
print(task_manager.read_task(3))
# update a task
print(task_manager.update_task(2, "Task 2 Updated", "This is task 2 updated"))
# delete a task
print(task_manager.delete_task(4))
