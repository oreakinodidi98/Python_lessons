# to view recursion limit 
from sys import getrecursionlimit, setrecursionlimit
print(f"Recursion limit is : {getrecursionlimit()}")
# set recursion limit
setrecursionlimit(2000)
print(f"\nNew recursion limit is : {getrecursionlimit()}")
#example 1 
def cut_cake(Number_of_friends, slices):
    # cut cake in half
    slices = slices * 2

    # check if there are enough slices for each friend
    if (slices >= Number_of_friends):
        # if there are enough slices, return number of slices
        return slices
    else:
        # if there are not enough slices, cut slices in half again
        return cut_cake(Number_of_friends, slices)

print(cut_cake(11, 1)) # 16

# example 2 factorial function
def factorial(n):
    # base case 0! = 1
    if n == 0:
        return 1
    else:
        # recursive case: n! = n * (n - 1)!
        return n * factorial(n - 1)

print(factorial(5)) # 120