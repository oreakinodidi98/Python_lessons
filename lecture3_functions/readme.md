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

## Defining new functions

A **function definition** specifies the name of a new function and the sequence of statements that run when the function is called. 

- `def` is a keyword that indicates that this is a function definition.
The name of the function is `print_lyrics`.
  - Anything that's a legal variable name is also a legal function name.
- The empty parentheses after the name indicate that this function doesn't take any arguments.
- The first line of the function definition is called the **header** -- the rest is called the **body**.
- The header has to end with a colon and the body has to be indented. By convention, indentation is always four spaces.
- The body of this function is two print statements; in general, the body of a function can contain any number of statements of any kind.

- Defining a function creates a **function object**
- The output indicates that `print_lyrics` is a function that takes no arguments. `__main__` is the name of the module that contains `print_lyrics`.
- we call it the same way we cal build in functions
- when it runs it executes the statment in the body

```py
def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print("I sleep all night and I work all day.")

print_lyrics # outputs <function __main__.print_lyrics()>
print_lyrics()
```

## parameters Vs argument

- paramters passed through the function header
- arguments are values passed to the function when called
- return statment: sending a message to where you called the function from
- Some of the functions we have seen require arguments; for example, when you call `abs` you pass a number as an argument.
- Some functions take more than one argument; for example, `math.pow` takes two, the base and the exponent.

Here is a definition for a function that takes an argument.

```py
def print_twice(string):
    print(string)
    print(string)

print_twice('Dennis Moore, ')

line = 'Dennis Moore, '
print_twice(line)
```

- The variable name in parentheses is a **parameter**. When the function is called, the value of the argument is assigned to the parameter.
- For example, we can call `print_twice` like this.
- You can also use a variable as an argument.

## Calling functions

- Once you have defined a function, you can use it inside another function.
- Bellow function takes 2 parameters

```py
def repeat(word, n):
    print(word * n)

spam = 'Spam, '
repeat(spam, 4) # Spam, Spam, Spam, Spam,

def first_two_lines():
    repeat(spam, 4)
    repeat(spam, 4)

first_two_lines() # Spam, Spam, Spam, Spam, 
                  # Spam, Spam, Spam, Spam,

def last_three_lines():
    repeat(spam, 2)
    print('(Lovely Spam, Wonderful Spam!)')
    repeat(spam, 2)

last_three_lines()  # Spam, Spam, 
                    # (Lovely Spam, Wonderful Spam!)
                    # Spam, Spam,

def print_verse():
    first_two_lines()
    last_three_lines()
```

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

## Variables and parameters are local

- When you create a variable inside a function, it is **local**, which
means that it only exists inside the function.
- For example, the following function takes two arguments, concatenates them, and prints the result twice.
- When `cat_twice` runs, it creates a local variable named `cat`, which is destroyed when the function ends.
- If we try to display it, we get a `NameError`
- Outside of the function, `cat` is not defined.
- Parameters are also local.
  - For example, outside `cat_twice`, there is no such thing as `part1` or `part2`.

```py
def cat_twice(part1, part2):
    cat = part1 + part2
    print_twice(cat)

line1 = 'Always look on the '
line2 = 'bright side of life.'
cat_twice(line1, line2)
```

## Stack diagrams

To keep track of which variables can be used where, it is sometimes useful to draw a **stack diagram**.
Like state diagrams, stack diagrams show the value of each variable, but they also show the function each variable belongs to.

Each function is represented by a **frame**.
A frame is a box with the name of a function on the outside and the parameters and local variables of the function on the inside.