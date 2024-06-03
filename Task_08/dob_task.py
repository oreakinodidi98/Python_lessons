# Initialize lists to store names and birthdates
firstnames = []
lastnames = []
date = []
month = []
year = []

# open DOB.txt file and read the content of the file
with open("DOB.txt", 'r') as file:
    content = file.read()
    print (f"Full Text: \n{content}")
    # Seek back to the beginning of the file
    file.seek(0)

    # Iterate over each line in the file
    for line in file:
        # Split the line into a list of words
        words = line.split()

        # Append the first word to the firstnames list
        firstnames.append(words[0])
        # Append the second word to the lastnames list
        lastnames.append(words[1])
        # Append the third word to the date list
        date.append(words[2])
        # Append the fourth word to the month list
        month.append(words[3])
        # Append the fifth word to the year list
        year.append(words[4])
    file.close()


# print out the firstname + lastnems
# Print out the names
print("\nName:")
for first, last in zip(firstnames, lastnames):
    print(first, last)

# Print out the birthdates
print("\nBirthdate:")
for d, m, y in zip(date, month, year):
    print(f"{d} {m} {y}")

    
