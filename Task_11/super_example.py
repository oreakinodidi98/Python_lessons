# define parent class
class Computer():
    def __init__(self, computer, ram, ssd):
        self.computer = computer
        self.ram = ram
        self.ssd = ssd
    
    def display(self):
        print(f"This computer is a {self.computer} ssd: {self.ssd}, with RAM of {self.ram}")

#define the subclass
class Laptop(Computer):
    def __init__(self, computer, ram, ssd, model):
    #super() is used to call the parent class constructor
        super().__init__(computer, ram, ssd)
        self.model = model

# create a laptop object
vivobool = Laptop("Asus", 8, 512, "VivoBook")

# print laptop features
print('Computer make:', vivobool.computer)
print('Computer model:', vivobool.model)
print(f"This computer has {vivobool.ram} GB of RAM ")
print(f"This computer has {vivobool.ssd} GB of SSD storage")