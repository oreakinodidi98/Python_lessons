##### build in functions######

print("Hello World!")
name = input("Please enter your name: ")
#----------------------------------
sorted_list = sorted([5,4,7,3,7,9,4,5,6,6,3,8,0,2,5,4,36,7,0])
print(sorted_list)
#----------------------------------
print(isinstance("This is a string!", str)) 
# to test what is the type of the variable 
#----------------------------------
rounded_number = round(23.4553254, 2)
print(rounded_number)
# round the number to 2 decimal places
#----------------------------------
num = pow(10, 5)
print(num)
# 10^5
#----------------------------------


############# Importing functions #############
from math import sqrt, gcd

print(sqrt(25))
# get the square root of 25 which is 5
print(gcd(5, 8, 8, 9, 17))
# get the greatest common divisor of the numbers

#----------------------------------
# this requires the tabulate module that you can install using pip install tabulate
from tabulate import tabulate

table = [["Peter", "Parker", 23],
         ["Carl", "Johnson", 33],
         ["Mike", "Nickleson", 28]]
my_headers = ["Name", "Surname", "Age"]
print(tabulate(table, headers=my_headers))
# prints a table with the headers

#----------------------------------

############# User-defined functions #############

def print_line():
    print("-"*80)
    # prints a line of 80 dashes

print_line()
print("We can now print lines!")
print_line()
# prints a line before and after the text

#----------------------------------

def print_menu(title, options):
    print_line()
    print((" "*(40-(len(title)//2))), title)
    print_line()
    for i, option in enumerate(options,  1):
        print(i, option, sep=" - ")

print_menu("Calculator", ["Add", "Subtract", "Multiply", "Divide"])
# prints a menu with the title and options
#----------------------------------

#Extend print_line and print_menu functionality above using default values
def print_line(symbol="-", length=80):
    print(symbol*length)


def print_menu(title, options, length):
    print_line(length=length)
    print((" "*((length//2)-(len(title)//2))), title)
    print_line(length=length)
    for i, option in enumerate(options,  1):
        print(i, option, sep=" - ")

print_menu("Calculator", ["Add", "Subtract", "Multiply", "Divide"], 20)

"""Returning values ********************* """

def add(num1, num2):
    return num1 + num2

result = add(5, 6)
# the result will be 11
result -= 3
# the result will be 8
print(result)
#----------------------------------
def fahrenheit_to_celsius(value):
    return (value-32) * 5/9

def celsius_to_kelvin(value):
    return value + 273.15

f_value = 60
c_value = fahrenheit_to_celsius(f_value)
k_value = celsius_to_kelvin(c_value)

print(f"{f_value}\xb0F is equal to {round(c_value,3)}\xb0C and {round(k_value,3)}K")
#----------------------------------
def cut_list(lst, section):
    # Calculate the midpoint index of the list
    mid = len(lst) // 2

    # If the section is "top", return the first half of the list
    if section == "top":
        return lst[:mid]
    # If the section is "bot", return the second half of the list
    elif section == "bot":
        return lst[mid:]

# Example usage: cut the list into the "top" section (first half)
print(cut_list([1, 2, 3, 4, 5, 6, 7, 5, 3, 5, 6, 45, 345], "top"))  
# Output: [1, 2, 3, 4, 5, 6]


"""Function Decorators *********************"""

# Define a decorator named `positives_only`
def positives_only(func):
    # Define a wrapper function that will modify the behavior of the original function
    def wrapper(values):
        # Filter out negative numbers from the input list `values`
        values = [i for i in values if i >= 0]
        # Call the original function `func` with the filtered list and return the result
        return func(values)
    # Return the wrapper function
    return wrapper

# Apply the `positives_only` decorator to the `average` function
@positives_only
def average(numbers):
    # Calculate and return the average of the numbers in the list
    return sum(numbers) / len(numbers)

# Test the `average` function with a list that includes negative numbers
print(average([-1, -5, -2, -6, 1, 5, 3, 2])) # Result: [1, 5, 3, 2] / 4 = 2.75


"""Recursion *********************"""
def add_numbers(numbers):
    if len(numbers) == 1:
        return numbers[0]
    else:
        return numbers[0] + add_numbers(numbers[1:])
    
print(add_numbers([1,2,3]))


"""Higher-order functions *********************"""

words = ["cat", "dog", "monkey", "lion", "tiger"]
print(sorted(words, key=len))   # len() function is passed as key
# key that we are sorting is the length of the words. default is ascending order
#----------------------------------
def filter_data(data, func):
    # Apply the given function `func` to each item in the `data` list and include
    # the item in the result list if `func(value)` returns True.
    return [i for i in data if func(i)]

def is_even(value):
    # Check if a given integer `value` is even. Return True if it is, otherwise False.
    return True if value % 2 == 0 else False

def is_digit(value):
    # Check if a given string `value` consists only of digits. Return True if it does, 
    # otherwise False.
    return True if value.isdigit() else False

# Filter the list of integers, keeping only even numbers
print(filter_data([1, 2, 3, 4, 5, 6, 7, 8, 9], is_even))  # Output: [2, 4, 6, 8]

# Filter the list of strings, keeping only those that are digits
print(filter_data(["1", "2", "s", "3", "4", "f", "gg", "s", "r", "5"], is_digit))  
# Output: ["1", "2", "3", "4", "5"]

"""Docstrings *********************"""

from math import pi

def calculate_area(radius : float) -> float:
    """
    Calculate the area of a circle.

    :param radius: The radius of the circle.
    :type radius: float
    :return: The area of the circle.
    :rtype: float
    """
    return pi * (radius**2)

print(calculate_area(4))

""" Built-In HOF reduce() *****************************

**************************************************************************
Reduce takes in a list of values and reduces it to one value that is the
accumulating(summed) results of feeding each number through an algorithm.
**************************************************************************

Parameters:

*A binary function: This function takes two arguments and defines the operation 
                    to be performed on the elements.
*An iterable:       The collection of elements that the function will be applied to.
*An optional initial value: This value serves as the starting point for 
                            the reduction process. If provided, the first call 
                            to the binary function will use this initial value 
                            and the first element of the iterable.
"""

# --------------  Original required code without using reduce()
# Example binary function (addition)
def add(x, y):
    return x + y

# Example iterable
numbers = [1, 2, 3, 4, 5]
start_with = 0
result = start_with

# Main Code
for number in numbers:
    x = result
    y = number
    result = add(x, y)

print(f"result: {result}") 

# --------------  Using HOF Reduce()
from functools import reduce

# Example binary function (addition)
def add(x, y):
    return x + y

# Example iterable
numbers = [1, 2, 3, 4, 5]

# Using reduce to sum the elements
result = reduce(add, numbers, 0)
print(f"result: {result}")  # Output: 15 0 + (1 + 2 + 3 + 4 + 5)


""" Built-in HOF filter() *****************************

**************************************************************************
It filters elements from an iterable (e.g., a list) based on a specified condition. 
It returns a new iterable containing only the elements for which 
the given condition is true.
**************************************************************************

Parameters:

*A function: This function should return a Boolean value (True or False). 
Each element of the iterable is passed to this function, 
and only the elements for which the function returns True 
are included in the result.
*An iterable: The collection of elements that you want to filter.
"""

# --------------  Using HOF filter()
# Example function (filter even numbers)
def is_even(num):
    return num % 2 == 0

# Example iterable
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using filter to get even numbers
result = filter(is_even, numbers)
print(f"result: {result}")      # Iterable object
"""
result variable above is an 'iterator object' and not readable as a whole, but
designed to be efficient and memory-friendly especially for large data sets. 
They provide elements one at a time, and they don't store the 
entire sequence of elements in memory. 
Instead, they generate each element on-the-fly as needed.
"""
filtered_numbers = list(result) # Cast to list to make readable as a whole
print(f"filtered numbers: {filtered_numbers}")  # Output: [2, 4, 6, 8, 10]

# for fun: how do we print the below without the [] brackets?
print("filtered numbers:", end=" ")
# Answer: 
print(*filtered_numbers, sep=", ")
# The * operator in the statement print(*filtered_numbers, sep=", ") 
# is used for unpacking the elements of the iterable filtered_numbers 
# and passing them as individual arguments to the print function.

""" Build-in HOF map() *****************************

**************************************************************************
It applies a given function to all items in an iterable (e.g., a list) 
and return a new iterable containing a result for each item in the list.
**************************************************************************

Parameters:

*A function: This function defines the operation to be applied to 
each element of the iterable.
*An iterable: The collection of elements that you want to process.
"""

# --------------  Using HOF map()
# Example function (square each number)
def square(num):
    return num ** 2

# Example iterable
numbers = [1, 2, 3, 4, 5]

# Using map to square each number
result = map(square, numbers)
print(f"result: {result}")      # Iterable object

# To re-use an iterable object, use itertools.tee   ---------
from itertools import tee
# Read original result and make copies
# Remember that result used for tee can't be read again, since the read pointer
# is at the end, but we created a copy by overwriting the same variable 
# with read pointer at the start and we can then use the new result again.
result_active, result = tee(result) 

squared_numbers = list(result_active)
print(f"squared numbers: {squared_numbers}")  # Output: [1, 4, 9, 16, 25]

#### Lambda functions -------------------

# --------------  Using HOF Reduce() with Lambda
from functools import reduce

# Example iterable
numbers = [1, 2, 3, 4, 5]

# Using reduce with a lambda function to sum the elements
result = reduce(lambda x, y: x + y, numbers)
print(result)  # Output: 15 (1 + 2 + 3 + 4 + 5)

# --------------  Using HOF filter() with Lambda
# Example iterable
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using filter with a lambda function to get even numbers
result = filter(lambda x: x % 2 == 0, numbers)
filtered_numbers = list(result)
print(filtered_numbers)  # Output: [2, 4, 6, 8, 10]

# --------------  Using HOF map() with Lambda
# Example iterable
numbers = [1, 2, 3, 4, 5]

# Using map with a lambda function to square each number
result_iterator = map(lambda x: x ** 2, numbers)

# Converting the iterator to a list for printing
result_list = list(result_iterator)

# Printing the result
print(result_list)  # Output: [1, 4, 9, 16, 25]

# **************************************************************************
# Additional Code:
# **************************************************************************

##### Additional use of lambda --------------
# --------------  Using Lambda with the sorted function
words = ['apple', 'banana', 'cherry', 'date']
sorted_words = sorted(words, key=lambda x: len(x)) # for x in words:
print(sorted_words)  # Output: ['date', 'apple', 'banana', 'cherry']

##### User-defined HOF function --------------

# Binary operation: Addition
def add(x, y):
    return x + y

# Unary operation: Square
def square(x):
    return x ** 2
    
def apply_operation_to_list(numbers, binary_operation, unary_operation):
    """
    Apply a binary operation element-wise to pairs of numbers from the list,
    and then apply a unary operation to each result.

    Parameters:
    - numbers: List of numbers.
    - binary_operation: Binary operation function taking two arguments.
    - unary_operation: Unary operation function taking one argument.

    Returns:
    - List of transformed values.
    """
    # Apply binary operation element-wise to pairs of numbers
    binary_results = [binary_operation(x, y) for x, y in zip(numbers[:-1], numbers[1:])]
    # numbers[:-1]: Takes all elements in the numbers list except the last one.
    # [1, 2, 3, 4]
    # numbers[1:]: Takes all elements in the numbers list except the first one.
    # [2, 3, 4, 5]
    # zip(): create pairs from these two slices [(1,2), (2,3), (3,4), (4,5)]

    # Apply unary operation to each result
    final_results = [unary_operation(result) for result in binary_results]

    return final_results

# Example usage:
numbers = [1, 2, 3, 4, 5]

# Applying the HOF with addition and square operations
result = apply_operation_to_list(numbers, add, square)