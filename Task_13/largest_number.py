def largest_number(number):
    # Base Case, if length of number is 1, then largest will always be the first number
    if len(number) == 1:
        # return the first element in the list
        return number[0]
    else:
        # if length of number is not 1, check if the first element is greater than the second element
        if number[0] > number[1]:
            # if the first element is greater than the second element, remove the second element
            number.pop(1)
        else:
            # if the first element is not greater than the second element, remove the first element
            number.pop(0)
        #this will loop untill the length of the number is 1
        # call the function recursively with the modified list
        return largest_number(number)
# test the function
print(largest_number([10,2,5,3,12,16])) # 16