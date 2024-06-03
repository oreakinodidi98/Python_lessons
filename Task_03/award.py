#print out purpose of programm
print("This program will read in the times (in minutes) for all three events of a triathlon, namely swimming, cycling, and running, and then calculate and display the total time taken to complete the triathlon")
#ask user to input time for swimming
swimming_time = int(input("Enter the time taken for swimming (in minutes): "))
#ask user to input time for cycling
cycling_time = int(input("Enter the time taken for cycling (in minutes): "))
#ask user to input time for running
running_time = int(input("Enter the time taken for running (in minutes): "))
#calculate total time taken to complete the triathlon
total_time = swimming_time + cycling_time + running_time
print("The total time taken to complete the triathlon is:", total_time, "minutes")
# if statment to check what awards the user will get 
if total_time < 100:
    print("You have won a Provincial colours!")
# if total time is less than 105 but greater than 101
elif total_time < 105:
    print("You have won a Provincial half colours!")
# if total time is less than 110 but greater than 106
elif total_time < 110:
    print("You have won a Provincial scroll!")
# if total time is greater than 111 minutes
else:
    print("You have won No award!")