import unittest
from example2 import sum_list, get_first_sorted_name, get_middle_of_list, recursive_word_flip, get_all_students_average_grade

class TestSumList(unittest.TestCase):
    def test_sum_list(self):
        # arrange
        num_list = [1, 2, 3, 4, 5]
        #act
        result = sum_list(num_list)
        #assert
        self.assertEqual(result, 15)

    def test_sum_list_empty(self):
        # arrange
        num_list = []
        #act
        result = sum_list(num_list)
        #assert
        self.assertEqual(result, 0)

    def test_sum_list_two_numbers(self):
        # arrange
        num_list = [1, 2]
        #act
        result = sum_list(num_list)
        #assert
        self.assertEqual(result, 3)
        
    def test_get_first_sorted_name(self):
        # arrange
        names = ["John", "Alice", "Andrew", "Zoe"]
        #act
        result = get_first_sorted_name(names)
        #assert
        self.assertEqual(result, "Alice")

    def test_get_middle_of_list_odd(self):
        # arrange
        num_list = [1, 2, 3, 4, 5]
        #act
        result = get_middle_of_list(num_list)
        #assert
        self.assertEqual(result, 3)

    def test_get_middle_of_list_even(self):
        # arrange
        num_list = [1, 2, 3, 4]
        #act
        result = get_middle_of_list(num_list)
        #assert
        self.assertEqual(result, (2, 3))

    def test_get_middle_of_list_empty(self):
        # arrange
        num_list = []
        #act
        result = get_middle_of_list(num_list)
        #assert
        self.assertEqual(result, None)

    def test_grade_average_with_empty_list(self):
        # arrange
        student_grades = []
        #act
        result = get_all_students_average_grade(student_grades)
        #assert
        self.assertEqual(result, None)

    def test_grade_average_with_one_student(self):
        # arrange
        student_grades = [[90, 80, 70]]
        #act
        result = get_all_students_average_grade(student_grades)
        #assert
        self.assertEqual(result, 80)

class Testrecursivewordflip(unittest.TestCase):
    def test_recursive_word_flip(self):
        # arrange
        word = "hello"
        #act
        result = recursive_word_flip(word)
        #assert
        self.assertEqual(result, "olleh")
        
if __name__ == '__main__':
    unittest.main()