"""
write a function to enerate the nth Fibonacci number.
The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones, starting from 0 and 1.
* fibonacci(0) = 0
* fibonacci(1) = 1
* fibonacci(n) = fibonacci(n-1) + fibonacci(n-2) for n>1
example: 
fibonacci(2) = fibonacci(1) + fibonacci(0) = 1 + 0 = 1
fibonacci(3) = fibonacci(2) + fibonacci(1) = 1 + 1 = 2
fibonacci(4) = fibonacci(3) + fibonacci(2) = 2 + 1 = 3  
fibonacci(5) = = 3 + 2 = 5 
fibonacci(6) = 5 + 3 = 8
"""

# iteration method 
def fibonacci(n):
    # base case, if n is 0 or 1, return n
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # recursive case: calculate fibonacci recursively
    else:
        return fibonacci(n-1) + fibonacci(n-2) 

# test the function
print(fibonacci(7)) # 13


def fibonacci_itterative(n):
    # base case
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    fiv_prev = 0
    fiv_current = 1
# underscore is a common convention for unused variables name 
    for _ in range(2, n+1):
        # range that starts from 2 because we already have the first two numbers, and ends at n+1 because range is exclusive and does not include the last number
        fiv_next = fiv_prev + fiv_current
        fiv_prev = fiv_current
        fiv_current = fiv_next
        # can alwo be written as fiv_prev, fiv_current = fiv_current, fiv_next
    return fiv_current

print(fibonacci_itterative(6)) # 8