# Create a program that calculates shipping costs based on package weight, destination, and priority.
# Use if-elif-else statements to implement the following shipping rules:
# - Standard shipping: $5 base + $2 per kg
# - Express shipping: $15 base + $4 per kg  
# - International adds $10 to any shipping method
# - Free shipping if order value > $100 and weight < 2kg
# - Maximum shipping cost is capped at $50

packages = [
    {"weight": 1.5, "destination": "domestic", "priority": "standard", "value": 120},
    {"weight": 3.2, "destination": "international", "priority": "express", "value": 80},
    {"weight": 0.8, "destination": "domestic", "priority": "express", "value": 150},
    {"weight": 5.0, "destination": "international", "priority": "standard", "value": 200},
    {"weight": 2.5, "destination": "domestic", "priority": "standard", "value": 45}
]

# Write your conditional logic here to calculate shipping costs for each package:
shipping_costs = []

for package in packages:
    # Extract the values you need
    weight = package["weight"]
    destination = package["destination"]
    priority = package["priority"]
    value = package["value"]

    if value > 100 and weight < 2:
        cost = 0  # Free shipping condition
    else:
        if priority =="standard":
            cost = 5 + 2 * weight
        elif priority == "express":
            cost = 15 + 4 * weight
    
    if destination == "international":
        cost += 10 # type: ignore
   
    if cost > 50: # type: ignore
        cost = 50
    
    shipping_costs.append(cost) # type: ignore
# Print the shipping costs for each package
print(shipping_costs)
# Expected results: [0, 37.8, 0, 25, 10]