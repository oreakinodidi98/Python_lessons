def sum_list(lst):
    total = 0
    for num in lst:
        # Check if the element is a number
        if isinstance(num, str):
            # If the element is a string, return None
            return None
        # Add the number to the total sum
        total += num
    return total

# print(sum_list([1, 2, 3, 4, 5])) # 15


def get_first_sorted_name(names):
    # Sort the list of names alphabetically
    names.sort()
    # Get the first name in the sorted list and return it as the result
    name = names[0]
    # Return the first name in the sorted list
    return name


# arrange
names = ["John", "Alice", "Bob", "Zoe"]
#act
result = get_first_sorted_name(names)
#assert
print(result)# Alice
print (result == "Alice")

def get_middle_of_list(lst):
    # Get the length of the list
    length = len(lst)
    if lst:
        # Check if the length of the list is odd
        if length % 2 != 0:
            # If the length of the list is odd, return the middle element
            return lst[length // 2]
        # If the length of the list is even, return the two middle elements
        return lst[length // 2 - 1], lst[length // 2]
    # If the list is empty, return None
    return None

def get_average(grades):
    return sum(grades) / len(grades)

def get_all_students_average_grade(student_grades):
    # Check if the list of student grades is not empty
    if student_grades:
        # If the list of student grades is empty, return None
        grade_average = 0
        # Calculate the average grade for each student
        for grades in student_grades:
            # Add the average grade to the total sum
            grade_average += get_average(grades)
            # Calculate the average grade for all students
        grade_average = round(grade_average / len(student_grades), 2)
        # Return the average grade for all students
        return grade_average
    return None

# recursive function
def recursive_word_flip(word):
    # Check if the length of the word is less than or equal to 1
    if len(word) <= 1:
        # If the length of the word is less than or equal to 1, return the word
        return word
    # If the length of the word is greater than 1, return the word in reverse order
    else:
        # Return the last letter of the word and call the function recursively
        return recursive_word_flip(word[1:]) + word[0]

print(recursive_word_flip("hello")) # "olleh"