import unittest
#The TodoList class, which represents the functionality to be tested, is in a separate file (todo_list.py), promoting modularity
from todo_list import TodoList
#The TodoList class is imported into the test file (test_todo_list.py), allowing access for testing

class TestTodoList(unittest.TestCase):
    #The TestTodoList class inherits from unittest.TestCase, and each test is a test-case method
    
    def setUp(self):
        # Create a new TodoList instance before each test
        self.todo_list = TodoList()

    def test_add_task(self):
        # Test if add_task method correctly adds a task
        self.todo_list.add_task("Task 1")
        # Check if the tasks list contains the added task
        self.assertEqual(self.todo_list.tasks, [])
        # A failing test case is intentionally created by checking for the incorrect tasks list after adding a task
        # should be self.assertEqual(self.todo_list.tasks, ["Task 1"])

    def test_update_task(self):
        # Test if update_task method correctly updates an existing task
        self.todo_list.add_task("Task 1")
        # Add a task to the list before updating it
        self.todo_list.update_task("Task 1", "Updated Task 1")
        # Update the task in the list
        self.assertEqual(self.todo_list.tasks, ["Updated Task 1"])
        # Check if the tasks list contains the updated task

    def test_remove_task(self):
        # Test if remove_task method correctly removes a task
        self.todo_list.add_task("Task 1")
        # Add a task to the list before removing it
        self.todo_list.remove_task("Task 1")
        # Remove the task from the list
        self.assertEqual(self.todo_list.tasks, [])
        # Check if the tasks list is empty after removing the task

if __name__ == '__main__':
    unittest.main()

