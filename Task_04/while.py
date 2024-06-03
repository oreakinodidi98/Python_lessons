# set variables of total and count to 0
total = 0
count = 0
# while loop to ask user to input a number
while True:
# ask user to input a number
    num = int(input("Enter a number (enter -1 to stop): "))
# if the user inputs -1, the loop will break
    if num == -1:
        break
# add the number to the total
    total += num
# add 1 to the count
    count += 1
# if the count is greater than 0, the average will be calculated and printed
if count > 0:
    average = total / count
    print("Average of the entered numbers is:", average)
else:
# if the count is 0, the user will be told that no numbers were entered
    print("No numbers were entered.")