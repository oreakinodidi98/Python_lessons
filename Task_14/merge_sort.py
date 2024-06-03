# merge sort
def merge_sort(items):
    n = len(items)
    temporary_storage = [None] * n
    #slpit into subsections of size 1
    size_of_subsections = 1
# finds the midpoint of the list and splits it into two halves until all the elements are in their own subsections
    while size_of_subsections < n:
        # for loop starting from 0 to n with a step of 2*size_of_subsections
        for i in range(0, n, 2 * size_of_subsections):
            # get the start and end of the first subsection
            i1_start, i1_end = i, min(i + size_of_subsections, n)
            # get the start and end of the second subsection
            i2_start, i2_end = i1_end, min(i1_end + size_of_subsections, n)
            # get the sections using the start and end of the subsections
            sections = (i1_start, i1_end), (i2_start, i2_end)
            # merge the subsections
            merge(items, sections, temporary_storage)
        size_of_subsections *= 2
    return items

def merge(items, sections, temporary_storage):
    (start_1, end_1), (start_2, end_2) = sections
    i_1 = start_1
    i_2 = start_2
    i_t = 0

    while i_1 < end_1 or i_2 < end_2:
        if i_1 < end_1 and i_2 < end_2:
            if len(items[i_1]) >= len(items[i_2]):
                temporary_storage[i_t] = items[i_1]
                i_1 += 1
            else:
                temporary_storage[i_t] = items[i_2]
                i_2 += 1
            i_t += 1
        elif i_1 < end_1:
            for i in range(i_1, end_1):
                temporary_storage[i_t] = items[i_1]
                i_1 += 1
                i_t += 1
        else:
            for i in range(i_2, end_2):
                temporary_storage[i_t] = items[i_2]
                i_2 += 1
                i_t += 1
    
    for i in range(i_t):
        items[start_1 + i] = temporary_storage[i]

# 3 string list example with length of at least 10 string elements and sort by length of string
items = ["Dog", "Ant", "Bird", "Elephant", "Cattegory", "Zebra", "Lion", "Tiger", "Monkey", "Giraffe"]
print(merge_sort(items))
items = ["Zebra", "Lion", "Tiger", "Monkey", "Giraffe", "Horse", "Rabbit", "Kangaroo", "Penguin", "Dolphin"]
print(merge_sort(items))
items = ["Horse", "Rabbit", "Kangaroo", "Penguin", "Dolphin", "Dog", "Ant", "Bird", "Elephant", "Cattegory"]
print(merge_sort(items))