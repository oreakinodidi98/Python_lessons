# create a list called menu , with items sold in a cafe
menu = ["coffee", "tea", "cake", "sandwich", "soup", "salad", "scone", "muffin", "croissant", "panini"]
# create a dictionry called stock, with the stok amount of each item in the menu
stock = {"coffee": 5, "tea": 10, "cake": 100, "sandwich": 30, "soup": 40, "salad": 50, "scone": 30, "muffin": 60, "croissant": 90, "panini": 30}
# create a dictionary called prices, with the value of each item in the menu
prices = {"coffee": 2.50, "tea": 2.00, "cake": 3.00, "sandwich": 4.00, "soup": 3.50, "salad": 4.50, "scone": 2.50, "muffin": 2.00, "croissant": 2.50, "panini": 4.50}

# calucluate item value for all ltems on the menu
for item in menu:
    item_value = stock[item] * prices[item]
    print(f"The value of {item} is: ${item_value}")
    # calculate the total value of all items on the menu
    total_value = sum(stock[item] * prices[item] for item in menu)
print(f"The total value of all items on the menu is: ${total_value}")