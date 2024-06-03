# import unitest
import unittest
# import the function from the buisness logic file
from buisness_logic import TaskManager
#import the ListRepository class from the data_access file
from data_access import ListRepository

# create a class named TestTaskManager
class TestTaskManager(unittest.TestCase):
    # create a setup function
    def setUp(self):
        # initialize the task manager
        self.task_manager = TaskManager()
        self.list_manager = ListRepository()
        # create a new task
        # self.task_manager.save_current_task(1, "Task 1", "Description 1", "high", "active")
        # self.task_manager.save_current_task(2, "Task 2", "Description 2", "medium", "inactive")
        # self.task_manager.save_current_task(3, "Task 3", "Description 3", "low", "active")
    
    # create a test function to test the get_tasks function
    def test_get_tasks(self):
        # check if the get_tasks function returns the correct tasks
        #arrange
        self.list_manager.task_data.append(ListRepository(1, "Task 1", "Description 1", "high", "active"))
        #act
        result = self.task_manager.get_all_tasks()
        length = len(self.list_manager.task_data)
        #assert
        self.assertEqual(length, 1)
        self.assertEqual(result, "\nTask ID: 1, Title: Task 1, Description: Description 1")
        #self.assertEqual(result, "\nTask ID: 1, Title: Task 1, Description: Description 1\nTask ID: 2, Title: Task 2, Description: Description 2\nTask ID: 3, Title: Task 3, Description: Description 3")
    
    # create a test function to test the save_task function
    def test_save_task(self):
        # check if the save_task function returns the correct message
        #act
        result = self.task_manager.save_current_task(4, "Task 4", "Description 4", "high", "active")
        #assert
        self.assertEqual(result, f"\nTask 4 is added successfully !")
    
    # create a test function to test the search_task function
    def test_search_task(self):
        # check if the search_task function returns the correct task
        #arrange
        self.list_manager.task_data.append(ListRepository(1, "Task 1", "Description 1", "high", "active"))
        #act
        result = self.task_manager.search_current_task(7)
        #assert
        self.assertEqual(result, "\nTask with ID 7 is not found!")
        
    
    # create a test function to test the update_task function
    def test_update_task(self):
        # check if the update_task function returns the correct message
        #arrange
        self.list_manager.task_data.append(ListRepository(3, "Task 1", "Description 1", "high", "active"))
        #act
        result = self.task_manager.update_current_task(3, "Task 3", "Description 3", "high", "inactive")
        #assert
        self.assertEqual(result, f"\nTask with ID 3 is updated successfully at: {self.list_manager.updated_at}!")
        
    
    # create a test function to test the delete_task function
    def test_delete_task(self):
        # check if the delete_task function returns the correct message
        #arrange
        self.list_manager.task_data.append(ListRepository(2, "Task 1", "Description 1", "high", "active"))
        #act
        result = self.task_manager.delete_current_task(2)
        #assert
        self.assertEqual(result, "\nTask with ID 2 is deleted successfully!")
        
if __name__ == '__main__':
    unittest.main()