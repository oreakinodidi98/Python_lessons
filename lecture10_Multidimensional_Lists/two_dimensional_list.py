grayscale_image =  [
                    [0, 0, 0, 0, 0],
                    [0, 1, 1, 1, 0],
                    [0, 1, 0, 1, 0],
                    [0, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0]
                    ]
# display imagge
for row in grayscale_image:
    print(row)
print("\n")

# example to dynamically create a 2D list
rows = 4
columns = 2
# create a 2D list with 3 rows and 2 columns
two_d_list = [[0 for column in range(columns)] for row in range(rows)]
print(two_d_list)

empty_gird = [[None] * columns for _ in range(rows)]
print(empty_gird)

#list of student scores
student_scores = [
                    [99, 90, 80, 70],
                    [41, 83, 71, 10],
                    [44, 80, 70, 60],
                    [22, 70, 60, 50]
                ]
# for lop to print the student scores
row_index = 0
for row in student_scores:
    print(f"Term {row_index + 1} scores are:") # row_index is used to display the term number
    for col in row:
        print(col, end="% ") # end is used to print the scores in the same line
    row_index += 1
    print("\n")

# ragged list example
ragged_list = [[1, 2, 3], 
               [4, 5], 
               [6, 7, 8, 9]]
# print every element in the ragged list
rows = len(ragged_list)
for row in range(rows):
    columns = len(ragged_list[row]) # number of columns in the row depends on the number of elements in the row
    print(f"Row {row} has {columns} columns")
    for col in range(columns):
        print(ragged_list[row][col], end=" ")
    print("\n")