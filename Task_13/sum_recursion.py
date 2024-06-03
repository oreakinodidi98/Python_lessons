def add_recursion(number, n):
    # Base Case, if n is 0 it will always be the first number
    if n == 0:
        # if n is 0, return the first element in the list
        return number[0]
    else:
        # if n is not 0, add the element at index n to the element at index n - 1
        # call the function recursively with n - 1
        return number[n] + add_recursion(number, n - 1)

print(add_recursion([10,2,5,3,12,16], 2)) # 25