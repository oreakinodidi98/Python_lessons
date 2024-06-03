#cnstant time complexity
def get_value(my_list, Key):
    return my_list[Key]

print(get_value([1, 2, 3, 4, 5], 2)) # 3

def get_value(my_list, Key):
    values =[]
    for i in Key:
        values.append(my_list[i])
    return values

print(get_value([1, 2, 3, 4, 5], [2, 3])) # [3, 4]
# linear time complexity : O(n)

def print_list(my_list):
    # sort the list O(nlog(n))
    my_list.sort()
    # iterate through the list O(n)
    for i in my_list:
        print(i)
    # total time complexity: O(nlog(n)) + O(n) = nlog(n)
    return

def display_print(list):
    # iterate through the list O(n)
    for _ in range(len(list)):
        # iterate through the list O(n)
        for item in list:
            print(item)
    # total time complexity: O(n) * O(n) = O(n^2) = n * n
    return

print(display_print([1, 2, 3, 4, 5]))
