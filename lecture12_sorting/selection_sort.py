def selection_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        min_index = i
        # Find the minimum element in remaining unsorted array
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]
        
# test the function
my_list = [64, 34, 25, 12, 22, 11, 90]
selection_sort(my_list)
print (f"Sorted array in ascending order:{my_list}")