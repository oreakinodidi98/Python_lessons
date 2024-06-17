# function

- functions are there to reduce repeated code
- named block of code that can be called and reused mmultiple times
- e.g. a recipe
- contains a set of instructions to create a dish
- can be used multiple times
- sets: defined operations
- A Union B
- intersection of A and B
- Difference between Set A and Set B
- Complement all the sets of A
- to execute a function

```py
def add (num1 ,num2):
    """This function adds two numbers together and returns the result."""
    return num1 + num2
# arguments 

print(add(5, 3))
"""so 5 and 3 are arguments of the function add, and num1 and num2 are parameters of the function add."""
sum_value = add(5, 3)
```

## parameters Vs argument

- paramters passed through the function header
- arguments are values passed to the function when called
- return statment: sending a message to where you called the function from

## function types

- built in functions
  - simply call and guive inforation
  - print ()
  - len()
  - max()
  - min()
- user efiened functions
  - functions you create yourself for specific task

## scope

- accesibility of variables in different parts of a program
- global scope
  - variables or functions defined outside of any function or class
- local scope
  - variables or functions defined inside of any function or class
  - can only be accesed inside the function and not visible outside of it
- block scope

## stack traces

- generated when an error occurs in pthon
- show the sequence of function calls leading up to the error
- Error type: syntax, Name , Type Error
- Error message: description of error , providing error message
- Traceback: list of function calls

```py
def divide (a, b);
    return a/b
# return keyword is optional
def main():
    result = divide (10, 0)
    print (result)

main()
```

## debugging

- identifying or fixing errors in our programm

## Revision notes

- Called methods when used in OOP Classes
- Functions help organise code, make it more readable, and facilitate debugging and maintenance
- Functions with two required positional inputs
  - my_function(input1, input2)
- Functions with one required positional input and one optional keyword input:
  - my_function(input1, keyword_arg=input2)

## built in functions

```bash
print("Hello, World")
print(len("hello"))
print(list(range(5)))
```

## creating Custom Functions

```bash
def greet(name):
  return f"hello, {name}!"

print(greet("allice"))
####################################
def square(number):
  return number*number

result=square(4)
print(result)
```

## HOF , High order Function

- A function that takes other functions as arguments or returns a function
- Accepting a function as an argument, altering it, and then returning the altered function

```py
numbers = [1, 2, 3, 4, 5]
# using squaed
squared = list(map(lamba x: x * x, numbers))
print(squared)
# using filter
evens = list(filter(lamba x: x % 2 == 0, numbers))
print(evens)
# using reduce -. one answer back
from functools import reduce
total = reduce(lamba x, y: x + y, numbers)
print(total)
```

## best practise for dunctions

- Descriptive Function Names
- Single Responsibility Principle: One function, one responsibility
- Avoiding Global Variables
- include Docstrings