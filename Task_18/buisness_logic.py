# import list repository form data_access
#from data_access import ListRepository
# import list properties from file_access
from file_access import ListRepository

# Create a class named TaskManager
class TaskManager:
    
    
    # Create a class named TaskManager
    def __init__(self):
        # initialize the task Task manager with a listrepository
        self.list_repository = ListRepository()


    def get_all_tasks(self):
        #Retrieve all tasks from the data source
        return self.list_repository.get_tasks()


    def save_current_task(self, file_id, file_title, description, priority, status):
        #save a task to the data sink
        # create new ID for the task
        new_id = len(self.list_repository.task_data) + 1
        # check if iD is already in the list
        for task in self.list_repository.task_data:
            if task['task_id'] == new_id:
                new_id += 1
        #set file_id to new_id
        self.file_id = new_id
        return self.list_repository.save_task(new_id, file_title, description, priority, status)
    

    def search_current_task(self, file_id):
        #read and display task based of ID
        return self.list_repository.search_task(file_id)
    

    def update_current_task(self, file_id, file_title, description, priority, status):
        #update task based on ID
        return self.list_repository.update_task(file_id, file_title, description, priority, status)
    

    def delete_current_task(self, file_id):
        #delete task based on ID
        return self.list_repository.delete_task(file_id)