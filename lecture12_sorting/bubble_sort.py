# bubble sort
def bubble_sort(arr):
    for i in range(len(arr) -1, -1, -1):
        for j in range(1, i + 1):
            if arr[j - 1] > arr[j]:
                #swap the values
                arr[j -1], arr[j] = arr[j], arr[j - 1]
    return arr
# test the function
arr = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sort(arr))
"""
first i = lenght of array -1 = 6 
So J will iterate from 1 to 6
j = 1 -> J-1 = 0 so index position is 0 = 64 > 34 => swap 34, 64
we take arr[j -1] which is positio 0 = 64 and arr[j] which is position 1 = 34 and swap them
arr = [34, 64, 25, 12, 22, 11, 90]
j = 2 -> J-1 = 1 so index position is 1 = 64 > 25 => swap 25, 64
we take arr[j -1] which is position 1 = 64 and arr[j] which is position 2 = 25 and swap them
arr = [34, 25, 64, 12, 22, 11, 90]
j = 3 -> J-1 = 2 so index position is 2 = 64 > 12 => swap 12, 64
we take arr[j -1] which is position 2 = 64 and arr[j] which is position 3 = 12 and swap them
arr = [34, 25, 12, 64, 22, 11, 90]
j = 4 -> J-1 = 3 so index position is 3 = 64 > 22 => swap 22, 64
we take arr[j -1] which is position 3 = 64 and arr[j] which is position 4 = 22 and swap them
arr = [34, 25, 12, 22, 64, 11, 90]
j = 5 -> J-1 = 4 so index position is 4 = 64 > 11 => swap 11, 64
we take arr[j -1] which is position 4 = 64 and arr[j] which is position 5 = 11 and swap them
arr = [34, 25, 12, 22, 11, 64, 90]
j = 6 -> J-1 = 5 so index position is 5 = 64 > 90 => swap 90, 64
we take arr[j -1] which is position 5 = 64 and arr[j] which is position 6 = 90 and swap them
arr = [34, 25, 12, 22, 11, 64, 90]
i will be counting down from the last number of length of array -1 to 0
i = 5
j = 1 -> J-1 = 0 so index position is 0 = 34 > 25 => swap 25, 34
we take arr[j -1] which is position 0 = 34 and arr[j] which is position 1 = 25 and swap them
arr = [25, 34, 12, 22, 11, 64, 90]
j = 2 -> J-1 = 1 so index position is 1 = 34 > 12 => swap 12, 34
we take arr[j -1] which is position 1 = 34 and arr[j] which is position 2 = 12 and swap them
arr = [25, 12, 34, 22, 11, 64, 90]
j = 3 -> J-1 = 2 so index position is 2 = 34 > 22 => swap 22, 34
we take arr[j -1] which is position 2 = 34 and arr[j] which is position 3 = 22 and swap them
arr = [25, 12, 22, 34, 11, 64, 90]
j = 4 -> J-1 = 3 so index position is 3 = 34 > 11 => swap 11, 34
we take arr[j -1] which is position 3 = 34 and arr[j] which is position 4 = 11 and swap them
arr = [25, 12, 22, 11, 34, 64, 90]
"""