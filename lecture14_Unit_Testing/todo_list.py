# todo_list.py
class TodoList:

    def __init__(self):
        # Initialise an empty list to store tasks
        self.tasks = []
    
    def add_task(self, task):
        # Add a new task to the list
        self.tasks.append(task)
        
    def update_task(self, old_task, new_task):
        # Update an existing task in the list
        if old_task in self.tasks:
            index = self.tasks.index(old_task)
            self.tasks[index] = new_task
    
    def remove_task(self, task):
        # Remove a task from the list
        if task in self.tasks:
            self.tasks.remove(task)

    def get_tasks(self):
        # Return the list of tasks
        return self.tasks
    
    def get_task(self, index):
        # Return the task at the given index
        return self.tasks[index]
    
# create object of TodoList
todo_list = TodoList()
todo_list.add_task("Task 1")
todo_list.add_task("Task 2")
todo_list.add_task("Task 3")
print(todo_list.get_tasks())
todo_list.update_task("Task 2", "Task 4")  
print(todo_list.get_tasks())
todo_list.remove_task("Task 3")
print(todo_list.get_tasks())
print(todo_list.get_task(1))
