# test_suite.py
import unittest
from test_crud_example import TestCrudExample

suite = unittest.TestLoader().loadTestsFromTestCase(TestCrudExample) 
unittest.TextTestRunner().run(suite)