class HousePlan:
    # using special built in method __init__ to create the constructor. Allows the class to initialize the attributes of the objects which are created
    # self keyword is a reference to the current instance of the class, and is used to access variables that belongs to the class
    def __init__(self, u_size, u_type, u_room, u_floor):
        self.__window = 6
        self.__door = 3
        self.__room = 3
        # taken parameters which will be used to create the object, assign them to the attributes of the object
        self.size = u_size
        self.type = u_type
        self.room = u_room
        self.floor = u_floor

    #create a method to open door
    def open_door(self):
        print("Door is open")
    # create method for lightswitch
    def light_switch(self):
        print("Light is on")
    # create method for cleaning
    def clean(self):
        print("House is clean")

    def set_window(self, window):
        self.__window = window

    def set_door(self, door):
        self.__door = door

    def set_room(self, room):
        self.__room = room

    def get_window(self):
        return self.__window

    def get_door(self):
        return self.__door

    def get_room(self):
        return self.__room

    def __str__(self):
        return f"Window: {self.__window}, Door: {self.__door}, Room: {self.__room}"

h_size = input("Enter the size of the house you would prefer (smallm medium, large) : ")
h_type = input("Enter the type of house you would prefer (bungalow, duplex, mansion) : ")
h_room = int(input("Enter the number of rooms you would prefer (enter an integer value): "))
h_floor = int(input("Enter the number of floors you would prefer (enter an integer value): "))

# when we pass in the class name, it will trigger the __init__ method and create the object saved in the variable kitt_house
kitt_house = HousePlan(h_size, h_type, h_room, h_floor)
ore_house = HousePlan("Large", "Mansion", 6, 3)

# using . notation to access the attributes of the object
print(f"""
      \n==========================
      House size: {kitt_house.size}
      House type: {kitt_house.type}
      House room: {kitt_house.room}
      House floor: {kitt_house.floor}
      \n===========================
""")
# call other methods in class 
kitt_house.open_door()
print("\n==========================")
kitt_house.light_switch()
print("\n==========================")
kitt_house.clean()