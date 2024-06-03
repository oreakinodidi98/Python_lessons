# ask user to enter sentence , use variable str_manip
str_manip = input("Enter a sentence: ")
#display lenght of str_manip
print("The length of the sentence is:", len(str_manip))
#find last letter in the str_manip sentence
print("The last letter of the sentence is:", str_manip[-1])
#replace every occurance of the last letter in sr_manip with "@"
print("The sentence with the last letter replaced with '@' is:", str_manip.replace(str_manip[-1], "@"))
#find last 3 letters in the str_manip sentence, and print backwards
print("The last 3 letters of the sentence in reverse are:", str_manip[-3:][::-1])
#find first 3 letters in the str_manip sentence, and last two letters and print together
print("The first 3 letters and the last 2 letters of the sentence joined form:", str_manip[:3] + str_manip[-2:])
