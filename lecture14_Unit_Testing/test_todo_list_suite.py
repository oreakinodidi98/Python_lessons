# test_suite.py
import unittest
from test_todo_list import TestTodoList

suite = unittest.TestLoader().loadTestsFromTestCase(TestTodoList) 
unittest.TextTestRunner().run(suite)