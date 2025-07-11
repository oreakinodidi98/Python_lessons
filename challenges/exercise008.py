# Create a program that determines insurance premiums based on driver profiles and risk factors.
# Use conditional statements to implement the following insurance calculation rules:
# - Base premium by age: 18-25 ($800), 26-35 ($600), 36-50 ($400), 51+ ($350)
# - Add 30% if driving record has violations
# - Add 25% if vehicle age > 10 years
# - Add 15% if annual mileage > 15000
# - Subtract 10% if driver has safety course certification
# - Subtract 20% if vehicle has advanced safety features
# - Minimum premium is $300, maximum is $1500

drivers = [
    {"name": "Alex", "age": 22, "violations": True, "vehicle_age": 12, "mileage": 18000, "safety_course": False, "safety_features": True},
    {"name": "Beth", "age": 35, "violations": False, "vehicle_age": 3, "mileage": 8000, "safety_course": True, "safety_features": True},
    {"name": "Carlos", "age": 45, "violations": True, "vehicle_age": 15, "mileage": 12000, "safety_course": True, "safety_features": False},
    {"name": "Diana", "age": 60, "violations": False, "vehicle_age": 2, "mileage": 5000, "safety_course": False, "safety_features": True},
    {"name": "Eve", "age": 19, "violations": True, "vehicle_age": 8, "mileage": 25000, "safety_course": False, "safety_features": False}
]

# Write your conditional logic here to calculate insurance premiums:
fee =[]
premiums = 0
for driver in drivers:
    name = driver["name"]
    age = driver["age"]
    violations = driver["violations"]
    vehicle_age = driver["vehicle_age"]
    mileage = driver["mileage"]
    safety_course = driver["safety_course"]
    safety_features = driver["safety_features"]


    # Base premium by age
    if age < 26:
        premiums = 800
    elif age <= 35:
        premiums = 600
    elif age <= 50:
        premiums = 400
    else:
        premiums = 350
    
    if violations == True:
        premiums = premiums * 1.30
    if vehicle_age > 10:
        premiums = premiums * 1.25
    if mileage > 15000:
        premiums = premiums * 1.15
    if safety_course == True:
        premiums = premiums * 0.90
    if safety_features == True:
        premiums = premiums * 0.80

    if premiums > 1500:
        premiums = 1500
    elif premiums < 300:
        premiums = 300

    fee.append((premiums))

# Print the calculated insurance premiums for each driver
print(fee)
# Expected results: [1500, 432, 585, 280, 1196]