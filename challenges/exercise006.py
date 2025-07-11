# Create a program that determines student grades and academic status based on test scores and attendance.
# Use conditional statements to implement the following grading system:
# - Grade A: average >= 90 and attendance >= 95%
# - Grade B: average >= 80 and attendance >= 90% 
# - Grade C: average >= 70 and attendance >= 85%
# - Grade D: average >= 60 and attendance >= 80%
# - Grade F: anything below these thresholds
# - Add "Honor Roll" status if grade is A or B with perfect attendance (100%)
# - Add "Warning" status if attendance < 75% regardless of grade

students = [
    {"name": "Alice", "scores": [92, 88, 95], "attendance": 98},
    {"name": "Bob", "scores": [78, 82, 85], "attendance": 92},
    {"name": "Charlie", "scores": [65, 70, 68], "attendance": 88},
    {"name": "Diana", "scores": [95, 98, 93], "attendance": 100},
    {"name": "Eve", "scores": [45, 52, 48], "attendance": 70}
]

# Write your conditional logic here to determine grades and status:
results = []

for student in students:
    # extract values
    name= student["name"]
    scores = student["scores"]
    attendance = student["attendance"]

    # calculate average score
    average = sum(scores) / len(scores)

    # if statment for grade

    if average >= 90 and attendance >= 95:
        grade = "A"
        status = "Honor Roll" if attendance == 100 else ""
        #status = "Warning" if attendance < 75 else ""
    elif average >= 80 and attendance >= 90:
        grade = "B"
        status = "Honor Roll" if attendance == 100 else ""
        #status = "Warning" if attendance < 75 else ""
    elif average >= 70 and attendance >= 85:
        grade = "C"
        status = "Warning" if attendance < 75 else ""
    elif average >= 60 and attendance >= 80:
        grade = "D"
        status = "Warning" if attendance < 75 else ""
    else:
        grade = "F"
        status = "Warning" if attendance < 75 else ""
    # append results
    results.append((name, grade, status))
# Print the results
print(results)
for result in results:
    print(result)
# Expected results: [("Alice", "A", ""), ("Bob", "B", ""), ("Charlie", "C", ""), ("Diana", "A", "Honor Roll"), ("Eve", "F", "Warning")]