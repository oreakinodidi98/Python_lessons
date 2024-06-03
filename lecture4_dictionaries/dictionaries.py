# dictionaries
my_dict = {'name': 'Ore', 'age': 25, 'city': 'New York'}
print(my_dict)
My_dict1 = dict(name='Ore', age=25, city='London')
my_dict2 = dict(name='Ben', age=20, city='London')
print(My_dict1)
print(my_dict['name'])
x= my_dict.get('age')
print(x)
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())
# to check if a specific key is present in the dictionary
if 'name' in my_dict:
    print("yes,'name' is one of the keys in the dictionary")

my_dict.update({"age":2021})
print(my_dict)
car_dict = my_dict.copy()
print(car_dict)
car_dict = dict(my_dict)
print(car_dict)
class_list = {"child1": My_dict1, "child2": my_dict2, "child3": my_dict}
print(class_list)
print(class_list['child1'])
print(class_list['child1']['name'])