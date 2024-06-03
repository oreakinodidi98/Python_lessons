# test_suite.py
import unittest
from test_examples import TestSumList

suite = unittest.TestLoader().loadTestsFromTestCase(TestSumList) 
unittest.TextTestRunner().run(suite)