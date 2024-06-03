import unittest
#The Task class, which represents the functionality to be tested, is in a separate file (crud_example.py), promoting modularity
from crud_example import Task
#The Task class is imported into the test file (test_crud_example.py), allowing access for testing

class TestCrudExample(unittest.TestCase):
    #The TestCrudExample class inherits from unittest.TestCase, and each test is a test-case method

    def setUp(self):
        # Create a new Task instance before each test, and initialize the task object
        self.crud_example = Task(1, "Task 1", "This is task 1")
        self.crud_example.task_data = [Task(1, "Task 1", "This is task 1"), Task(2, "Task 2", "This is task 2")]

    def test_display_tasks(self):
        # Test if display_tasks method correctly displays tasks
        expected_output = "\nTask ID: 1, Title: Task 1, Description: This is task 1" \
                          "\nTask ID: 2, Title: Task 2, Description: This is task 2" 
        #act
        result = self.crud_example.display_tasks()
        #assert
        self.assertEqual(result, expected_output)
        # Check if the tasks are displayed correctly
        # self.assertEqual(self.crud_example.display_tasks(), expected_output)
    
    def test_read_task(self):
        # Test if read_task method correctly reads a task
        expected_output = "\nTask ID: 1, Title: Task 1, Description: This is task 1"
        #act
        result = self.crud_example.read_task(1)
        #assert
        self.assertEqual(result, expected_output)
        #self.assertEqual(self.crud_example.read_task(1), expected_output)

    def test_create_task(self):
        # Test if create_task method correctly creates a task
        expected_output = "\nTask 79 is added successfully!"
        #self.crud_example.create_task("Task 79", "This is task 79")
        # Check if the task is created successfully
        self.assertEqual(self.crud_example.create_task("Task 79", "This is task 79"), expected_output)
        # Check if the task is created successfully with the correct title
        self.assertEqual(self.crud_example.task_data[-1].title, "Task 79")
        # Check if the task is created successfully with the correct description
        self.assertEqual(self.crud_example.task_data[-1].description, "This is task 79")
        
        

    def test_update_task(self):
        # Test if update_task method correctly updates a task
        #self.crud_example.update_task(1, "Task 2", "This is task 2")
        expected_output = "\nTask with ID 1 is updated successfully!"
        # Check if the task is updated successfully
        self.assertEqual(self.crud_example.update_task(1, "Task 2", "This is task 2"), expected_output)
        # Check if the task is updated successfully with the correct title
        self.assertEqual(self.crud_example.task_data[0].title, "Task 2")
        # Check if the task is updated successfully with the correct description
        self.assertEqual(self.crud_example.task_data[0].description, "This is task 2")
       

    def test_delete_task(self):
        # Test if delete_task method correctly deletes a task
        expected_output = "\nTask with ID 1 is deleted successfully!"
        # Check if the task is deleted successfully
        self.assertEqual(self.crud_example.delete_task(1), expected_output)
        self.assertEqual(len(self.crud_example.task_data), 1)

if __name__ == '__main__':
    unittest.main()