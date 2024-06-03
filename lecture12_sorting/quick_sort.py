# quick sort
def quick_sort(arr, low, high):
    if low < high:
        # partition the array
        mid = partition(arr, low, high)
        # sort the left and right subarrays
        quick_sort(arr, low, mid - 1)
        quick_sort(arr, mid + 1, high)
    return arr

def partition(arr, low, high):
    # select the rightmost element as pivot
    pivot = arr[low]
    
    #loop through the array. move items up or down the array so that they are in the proper spot with regard to the pivot point
    while low < high:
        # move right
        while low < high and arr[high] >= pivot:
            high -= 1
        
        if low < high:
            arr[low] = arr[high]
            while low < high and arr[low] <= pivot:
                low += 1
            if low < high:
                arr[high] = arr[low]
    arr[low] = pivot
    return low

# test the function
arr = [64, 34, 25, 12, 22, 11, 90]
print(quick_sort(arr, 0, len(arr) - 1)) # [11, 12, 22, 25, 34, 64, 90]