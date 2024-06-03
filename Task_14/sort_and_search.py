input_list =[27, -3, 4, 5, 35, 2, 1, -40, 7, 18, 9, -1, 16, 100]
# linear search is more appropriate to use for the following input list
# since the list is not sorted
def linear_search(input_list, target):
    for index, value in enumerate(input_list):
        if value == target:
            print(f"Target {target} has been found")
            return f"This is the index: {index}"
    return -1

# test the function

target = 9
print(linear_search(input_list, target))

# Function to do insertion sort
def insertionSort(input_list):

    # Traverse through 1 to len(arr)
    for i in range(1, len(input_list)):

        key = input_list[i]

        # Move elements of arr[0..i-1], that are greater than key, to one position ahead of their current position
        # Compare key with each element on the left of it until an element smaller than it is found

        j = i-1
        while j >= 0 and key < input_list[j] :
                input_list[j + 1] = input_list[j]
                j -= 1
        # Place key at after the element just smaller than it.
        input_list[j + 1] = key


# test the function
insertionSort(input_list)
print ("\nSorted array in ascending order:")
print(input_list)

# implement binary search on sorted array
def binary_search(input_list, target):
    low = 0
    high = len(input_list) - 1
    # keep iterating unill low and high cross
    #return -1 if target is not found
    while low <= high:
        # find the middle element
        mid = (low + high) // 2
        # check if the middle element is the target
        if input_list[mid] == target:
            print(f"Target {input_list[mid]} has been found")
            return f"This is the index: {mid}"
        elif input_list[mid] < target:
            # if the target at midpoint is greater than the middle element, search the right half
            low = mid + 1
        else:
            # if the target at midpoint is less than the middle element, search the left half
            high = mid - 1
            # if the target is not found, return -1
    return -1

# test the function
target = 9
print(binary_search(input_list, target)) # 8

# you would use this algorithm in reall life when you have a sorted list and you want to find an element in the list
# examples include searching for a name in a phone book, searching for a word in a dictionary, searching for a word in a book, etc.