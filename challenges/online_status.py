#function named online_count that takes dictionary that maps from strings of names to the string "online" or "offline"
def online_count(status):
    # create a variable called count and set it to 0
    count = 0
    # create a for loop to iterate through the dictionary
    for value in status.values():
        # if the value is "online", increment the count by 1
        if value == "online":
            count += 1
    # return the count
    return count
# test the function
statuses = {"Alice": "online", "Bob": "online", "Eve": "online"}
print(online_count({"Alice": "online", "Bob": "offline", "Eve": "online"})) # 2
print(online_count(statuses)) # 3