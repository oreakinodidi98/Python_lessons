"""
*
**
***
****
*****
****
***
**
*
"""

# they all have * in common so we can use a for loop to print them
star = "*"
# we want to loop through 10 times
# creating a list with 10 items, 0 to 9
for i in range(10):
    #if i is greater or equal to 5, we want to loop through 5 times, print out the star pattern and add 1 to i
    if i >= 5:
        # removes 2 characters from the star variable as when we get to i=5 we have 6 stars and continue the patter to add 1 moe star after the print statment. so would print 4 stars but end up with 5 stars
        star = star[:-2]
    
    print(star)
    # add a star to the star variable
    star += "*"

# Method 2
cross = "+"
# we want to loop through 10 times creating a list with 10 items, 0 to 9
for i in range(10):
    print(cross)
    if i < 4:
        # add a star to the star variable
        cross += "+"
    else:
        # subtract a star from the star variable list
        cross = cross[:-1]