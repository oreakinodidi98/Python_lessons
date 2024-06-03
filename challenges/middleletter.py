# function named mid , that takes string as parameter
def mid(string):
    # check if the length of the string is odd
    if len(string) % 2 != 0:
        # return the middle character of the string
        return string[len(string) // 2]
    else:
        # return ""
        return ''
# test the function
print(mid("testing")) # "t"
print(mid("middle")) # ""
print(mid("abc")) # "b"