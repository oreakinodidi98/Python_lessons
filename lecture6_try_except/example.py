def validdate_input(value):
    if not isinstance(value, int):
        raise ValueError("Please only enter a valid number.")
    
try:
    validdate_input("hello")
except ValueError as e:
    print(f"Error: {e}")

# example 2
def add_numbers(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise ValueError("Please only enter an integer or a float .")
    return a + b 

print(add_numbers(2, 3))

try:
    add_numbers(2, "hello")
except ValueError as e:
    print(f"Error: {e}")