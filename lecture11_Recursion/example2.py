def factorial(n):
    # base case 0! = 1. if n is 0 r 1, return 1
    if n == 0 or n == 1:
        return 1
    # recursive case: ccalculate factorial recursively
    else:
        # recursive case: n! = n * (n - 1)!
        return n * factorial(n - 1)

print(factorial(5)) # 120
# 5! = 5 * 4!
"""
5 => 5 * factorial(4)
4 => 4 * factorial(3)
3 => 3 * factorial(2)
2 => 2 * factorial(1)
1 => 1

5 => 5 * 24 = 120
4 => 4 * 6 = 24 
3 => 3 * 2 = 6
2 => 2 * 1 =2
1 => 1
"""
print(factorial(10))

def factorial_itterative(n):
    result = 1
    # iterate from 1 to n and multiply each number with the result
    for i in range(1, n+1):
        # end with n+1 because range is exclusive, does not include the last number
        result = result * i
       # same code as above:  result *= i
    return result