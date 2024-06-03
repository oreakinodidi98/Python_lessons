# Function to do insertion sort
def insertionSort(arr):

    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        # Compare key with each element on the left of it until an element smaller than it is found
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        # Place key at after the element just smaller than it.
        arr[j + 1] = key
# test the function
arr = [12, 11, 13, 5, 6]
insertionSort(arr)
print ("\nSorted array in ascending order:")
print(arr)
for i in range(len(arr)):
    print ("% d" % arr[i])
    
"""
I will start at 1
key = 11 as arr[1] = 11
J = 0
while J >= 0 -> j is o so trure. And key < arr[0] , so 11 < 12 . meaning both are true => arr[1] = arr[0] = 12
we take 12 and shift it up to 11 position 
arr = [12, 12, 13, 5, 6]
j = -1
arr[j + 1] = arr[0] = key = so position 0 is = 11
arr = [11, 12, 13, 5, 6]
i = 2
key = 13 as arr[2] = 13
j = 1
while j >= 0 -> j is 1 so true. And key < arr[1] , so 13 < 12 . this is false so we break out of the loop
arr = [11, 12, 13, 5, 6]
i = 3
key = 5 as arr[3] = 5
j = 2
while j >= 0 -> j is 2 so true. And key < arr[2] , so 5 < 13 . this is true so we shift 13 to the right
arr = [11, 12, 13, 13, 6]
j = 1
while j >= 0 -> j is 1, so true. And key < arr[1] , so 5 < 12 . this is true so we shift 12 to the right
arr = [11, 12, 12, 13, 6]
j = 0
while j >= 0 -> j is 0, so true. And key < arr[0] , so 5 < 11 . this is true so we shift 11 to the right
arr = [11, 11, 12, 13, 6]
j = -1
arr[j + 1] = arr[0] = key = so position 0 is = 5
arr = [5, 11, 12, 13, 6]
i = 4
"""