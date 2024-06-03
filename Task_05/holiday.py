# get user input
cit_flight= input("enter the city you are flying to: ")
num_flight= int(input("enter the flight number: "))
rental_days= int(input("enter the number of days you will be renting the car: "))

# create function for hotel cost calculation using num_flight
def hotel_cost(num_flight):
    return num_flight * 140

# create function for plane_cost using cit_flight and if else for options
def plane_cost(cit_flight):
    if cit_flight == "New York":
        return 200
    elif cit_flight == "Auckland":
        return 700
    elif cit_flight == "Venice":
        return 500
    elif cit_flight == "Glasgow":
        return 300
    else:
        return 0
    
# create car_rental function using rental_days
def car_rental(rental_days):
    return rental_days * 100
# call all 3 functions to calculate holiday cost
holiday_cost = hotel_cost(num_flight) + plane_cost(cit_flight) + car_rental(rental_days)
# print out total cost of holiday
print(f"The total cost of your holiday is: $ {holiday_cost}, this includes the cost of the hotel ${hotel_cost(num_flight)}, plane ${plane_cost(cit_flight)} and car rental ${car_rental(rental_days)}.")