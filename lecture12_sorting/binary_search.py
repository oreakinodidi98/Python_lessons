# binary search only works if list is in order
# binary search is faster than linear search
# we start in the middle of the list and compare the target to the middle element
# if the target is greater than the middle element, we search the right half of the list
# if the target is less than the middle element, we search the left half of the list
# we continue this process until we find the target or the list is empty
# binary search is O(log n)

def binary_search(input_list, target):
    low = 0
    high = len(input_list) - 1
    # keep iterating unill low and high corss
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
input_list = [1, 2, 3, 4, 5, 7, 8]
target = 7
print(binary_search(input_list, target)) # 5
