# with parameter with return statments
def add (num1 ,num2):
    """This function adds two numbers together and returns the result."""
    return num1 + num2
# arguments 

print(add(5, 3))
"""so 5 and 3 are arguments of the function add, and num1 and num2 are parameters of the function add."""
sum_value = add(5, 3)

# without parameter
def uniqu_greet():
    """This function greets the user."""
    print(f"Hello!")

uniqu_greet()

random_variable = input("Enter a random sentece: ")
print(f"You entered: {random_variable}, good stuff")
print(f"nobody expects", random_variable)

count_variable = input("Enter how many times you will describe yourself: ")
print(f" you descrivbe your self as : \n {count_variable} \n Length of sentence is {len(count_variable)}")