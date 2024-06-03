# Unit Testing

- Unit testing is a software-testing approach that focuses on testing individual components (such as classes, functions, or modules) in isolation to ensure they perform as intended
- A unit = class, function or a module
- Unit tests are automated, executed frequently during development, and provide early detection of defects.
- The primary goal is to detect defects early in the development process by automating tests and executing them frequently.
- **TDD = Test-Driven Development**

## Principles of Unit Testing

- **Arrange-Act-Assert (AAA)**
- AAA is a pattern for organising and structuring unit tests.It is sometimes also called “Given-When-Then”.
- Components:
- **Arrange**: Set up the necessary preconditions and inputs.
  - arrange values that i want to test
  - these values are repeted and reinitialised for every test
- **Act**: Perform the action or behaviour being tested.
  - store result in variables
- **Assert**: Verify that the outcome is as expected.
  - expected behaviur occured
- Given -> when -> then
- **FIRST** Principle :  acronym representing the key principles of effective unit tests
- Components:
- **Fast**: Tests should run quickly to provide rapid feedback
- **Isolated/Independent**: Tests should not depend on each other to ensure isolation.
- **Repeatable**: Tests should produce consistent results when executed repeatedly.
- **Self-Validating**: Tests should have a clear pass/fail outcome without manual interpretation.
- **Timely**: Tests should be written in a timely manner, preferably before the code.

Example:

``` py
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
```

Test cases:

```py
import unittest
#The TodoList class, which represents the functionality to be tested, is in a separate file (todo_list.py), promoting modularity
from todo_list import TodoList

#The TodoList class is imported into the test file (test_todo_list.py), allowing access for testing

class TestTodoList(unittest.TestCase):
    def setUp(self):
        # Create a new TodoList instance before each test
        self.todo_list = TodoList()

    def test_add_task(self):
        # Test if add_task method correctly adds a task
        self.todo_list.add_task("Task 1")
        self.assertEqual(self.todo_list.tasks, [])
        #A failing test case is intentionally created in the test_add_task method by checking for the incorrect tasks list after adding a task

    def test_update_task(self):
        # Test if update_task method correctly updates an existing task
        self.todo_list.add_task("Task 1")
        self.todo_list.update_task("Task 1", "Updated Task 1")
        self.assertEqual(self.todo_list.tasks, ["Updated Task 1"])

    def test_remove_task(self):
        # Test if remove_task method correctly removes a task
        self.todo_list.add_task("Task 1")
        self.todo_list.remove_task("Task 1")
        self.assertEqual(self.todo_list.tasks, [])

if __name__ == '__main__':
    unittest.main()

#The TestTodoList class inherits from unittest.TestCase, and each test is a test-case method
```

## How to Run tests

- Create a Test suite

```py
# test_suite.py
import unittest
from test_todo_list import TestTodoList

suite = unittest.TestLoader().loadTestsFromTestCas(TestTodoList) unittest.TextTestRunner().run(suite)
```

- unit = behaviour of our program -> not each function but the feature that works togethere
- refacturing = making code better without changing function of the code
- 