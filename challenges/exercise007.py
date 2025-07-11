# Create a program that categorizes online orders and calculates processing fees based on multiple criteria.
# Use conditional statements to implement the following business rules:
# - Express orders (delivery < 24 hours): $15 fee
# - Standard orders (delivery 1-3 days): $5 fee  
# - Economy orders (delivery > 3 days): $2 fee
# - Add $8 fragile handling fee if item is fragile
# - Add $12 international shipping if not domestic
# - Apply 20% discount on total fees if customer is premium member
# - Minimum fee is $3, maximum fee is $50

orders = [
    {"item": "Electronics", "delivery_days": 1, "fragile": True, "location": "domestic", "premium": False},
    {"item": "Books", "delivery_days": 5, "fragile": False, "location": "international", "premium": True},
    {"item": "Glassware", "delivery_days": 2, "fragile": True, "location": "international", "premium": False},
    {"item": "Clothing", "delivery_days": 7, "fragile": False, "location": "domestic", "premium": True},
    {"item": "Artwork", "delivery_days": 1, "fragile": True, "location": "international", "premium": True}
]

# Write your conditional logic here to calculate processing fees:
processing_fees = []

fee = 0
for order in orders:
    item = order["item"]
    delivery_days = order["delivery_days"]
    fragile = order["fragile"]
    location = order["location"]
    premium = order["premium"]

    
    if delivery_days <= 1:
        fee = 15
    elif delivery_days <= 3:
        fee = 5
    else:
        fee = 2

    if fragile == True:
        fee += 8

    if location == "international":
        fee += 12

    if premium == True:
        fee *= 0.8
        
    if fee> 50: # type: ignore
        fee = 50
    elif fee < 3: # type: ignore
        fee = 3
    processing_fees.append(fee)
# Print the processing fees for each order
print(processing_fees)
# Expected results: [23, 11.2, 25, 3, 28]