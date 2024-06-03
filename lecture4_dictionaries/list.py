fruits = ['apple', 'banana', 'cherry']
# fruits.append("orange")
# print(fruits)
# fruits.extend(["mango", "kiwi"])
# print(fruits)
# print(len(fruits))
# fruits.insert(1, "lemon")
# print(fruits)
# fruits[0:1] = ["watermelon", "grape"]
# print(fruits)
# fruits_tuple = ("apple", "banana", "cherry", "orange")
# fruits.extend(fruits_tuple)
# print(fruits)
# print(type(fruits), type(fruits_tuple))
# #remove items
# removed_item = fruits.pop(1)
# print(removed_item)
# fruits.remove("apple")
# print(fruits)
# del fruits[0]

fruits.sort()
print(fruits)
#looping

for fruit in fruits:
    print(fruit)

for i in range(len(fruits)):
    print(fruits[i])

# while loop
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1