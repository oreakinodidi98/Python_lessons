#data_access.py

# import current_dataTime function from utilities.py
from utilities import current_dateTime, current_dateTime_day

# Create a class named ListRepository
class ListRepository:

    def __init__(self, filename='tasks.txt'):
        self.filename = filename
        self.task_data = self.load_data()
        # define file name
        self.filename = 'tasks.txt'

    #load file data
    def load_data(self):
        try:
            with open(self.filename, 'r') as file:
                lines = file.readlines()
                # Parse each line to reconstruct the task dictionary
                return [self.parse_task(line.strip()) for line in lines]
                #return lines
                #return [eval(line) for line in lines]   
        except FileNotFoundError:
            return []
        
    # save file data
    def save_data(self):
        with open(self.filename, 'a') as file:
            for task in self.task_data:
                # Convert the task dictionary into a string representation
                task_str = f"{task['task_id']}, {task['title']}, {task['description']}, {task['priority']}, {task['status']}, {task['created_at']}, {task['updated_at']}\n"
                # Write the task string to the file
                file.write(task_str)
                #close the file
                file.close()
                

    # get tasks
    def get_tasks(self):
        task_length = len(self.task_data)
        if task_length:
            tasks_info = ""
            for task in self.task_data:
                tasks_info += f"\n{task['task_id']}, {task['title']}, {task['description']}, {task['priority']}, {task['status']}, {task['created_at']}, {task['updated_at']}"
            return tasks_info
        return "Currently no tasks available!"
    
    # Helper method to parse a task string into a dictionary
    def parse_task(self, task_str):
        task_fields = task_str.split(',')
        return {
            'task_id': task_fields[0],
            'title': task_fields[1],
            'description': task_fields[2],
            'priority': task_fields[3],
            'status': task_fields[4],
            'created_at': task_fields[5],
            'updated_at': task_fields[6]
        }

    # save task
    def save_task (self,file_id, file_title, description, priority, status):
        new_task = {
            'task_id': file_id,
            'title': file_title,
            'description': description,
            'priority': priority,
            'status': status,
            'created_at': current_dateTime(),
            'updated_at': current_dateTime_day()
        }
        self.task_data.append(new_task)
        self.save_data()
        return f"\n{file_title} is added successfully !"
    
    # search task
    def search_task (self, file_id):
        task_length = len(self.task_data)
        if task_length:
            for task in self.task_data:
                if task['task_id'] == file_id:
                    return f"\nTask ID: {task['task_id']}, Title: {task['title']}, Description: {task['description']}, Priority: {task['priority']}, Status: {task['status']}, Created At: {task['created_at']}, Updated At: {task['updated_at']}"
            return f"\nTask with ID {file_id} is not found!"
        return "Currently no tasks available!"
    
    # update task
    def update_task (self, file_id, file_title, description, priority, status):
        task_length = len(self.task_data)
        if task_length:
            for task in self.task_data:
                if task['task_id'] == file_id:
                    task['title'] = file_title
                    task['description'] = description
                    task['priority'] = priority
                    task['status'] = status
                    task['updated_at'] = current_dateTime()
                    self.save_data()
                    return f"\nTask with ID {file_id} is updated successfully at: {task['updated_at']}!"
            return f"\nTask with ID {file_id} is not found!"
        return "Currently no tasks available to update!"
    
    # delete task
    def delete_task (self, file_id):
        task_length = len(self.task_data)
        if task_length:
            for task in self.task_data:
                if task['task_id'] == file_id:
                    self.task_data.remove(task)
                    self.save_data()
                    return f"\nTask with ID {file_id} is deleted successfully!"
            return f"\nTask with ID {file_id} is not found!"
        return "Currently no tasks available to delete!"
    