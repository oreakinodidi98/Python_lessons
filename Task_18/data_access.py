#data_access.py
# import current_dataTime function from utilities.py
from utilities import current_dateTime, current_dateTime_day

# Create a class named ListRepository
class ListRepository:

    # list to store tasks
    task_data = []
    # create a constructor
    def __init__(self, task_id=None, title=None, description=None, priority=None, status=None, created_at=None, updated_at=None):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.priority = priority
        self.status = status
        self.created_at = current_dateTime()
        self.updated_at = current_dateTime_day()

    def get_tasks(self):
        # Retrieve tasks from the data source
        # get length of the task_data list
        task_length = len(self.task_data)
        # if the task_data list is empty, return a message
        if task_length:
            # create an empty string to store the tasks
            tasks_info = ""
            # return the list of tasks
            for task in self.task_data:
                # add the task to the tasks_info string
                tasks_info += f"\nTask ID: {task.task_id}, Title: {task.title}, Description: {task.description}"
                # return the tasks_info
            return tasks_info
        return "Currently no tasks available!"
    

    # Create new task function
    def save_task (self,file_id, file_title, description, priority, status):
        # create new task
        new_task = ListRepository(file_id, file_title, description, priority, status, current_dateTime, current_dateTime_day)
        # add the new task to the list
        self.task_data.append(new_task)
        return f"\n{file_title} is added successfully !"
    

    def search_task (self, file_id):
        # get length of the task_data list
        task_length = len(self.task_data)
        # if the task_data list is empty, return a message
        if task_length:
            """read and display task based of ID"""
            for task in self.task_data:
                if task.task_id == file_id:
                    return f"\nTask ID: {task.task_id}, Title: {task.title}, Description: {task.description}, Priority: {task.priority}, Status: {task.status}, Created At: {task.created_at}, Updated At: {task.updated_at}"
                # if not found display message
            return f"\nTask with ID {file_id} is not found!"
        return "Currently no tasks available!"
    

    def update_task (self, file_id, file_title, description, priority, status):
        # get length of the task_data list
        task_length = len(self.task_data)
        # if the task_data list is empty, return a message
        if task_length:
            # update task based on ID
            for task in self.task_data:
                if task.task_id == file_id:
                    task.title = file_title
                    task.description = description
                    task.priority = priority
                    task.status = status
                    task.updated_at = self.updated_at
                    return f"\nTask with ID {file_id} is updated successfully at: {self.updated_at}!"
            # if not found display message
            return f"\nTask with ID {file_id} is not found!"
        # if the task_data list is empty, return a message
        return "Currently no tasks available to update!"
    

    def delete_task (self, file_id):
        # get length of the task_data list
        task_length = len(self.task_data)
        # if the task_data list is empty, return a message
        if task_length:
            # delete task based on ID
            for task in self.task_data:
                if task.task_id == file_id:
                    self.task_data.remove(task)
                    return f"\nTask with ID {file_id} is deleted successfully!"
            # if not found display message
            return f"\nTask with ID {file_id} is not found!"
        return "Currently no tasks available to delete!"