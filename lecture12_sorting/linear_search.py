# linear search used when the list is not sorted
# start by knowing what element we want to find and then iterate over the list to find the element
# if the element is found, return the index of the element
# if the element is not found, return -1
def linear_search(input_list, target):
    for index, value in enumerate(input_list):
        if value == target:
            return index
    return -1

# test the function
input_list = [4, 3, 2, 8, 7, 5, 1]
target = 7
print(linear_search(input_list, target))