class MathUtil:
    # decorator method, this is a method that belongs to the class and not the object
    @staticmethod
    # dont need an instance to call the static method
    def add(a, b):
        return a + b
    
    @staticmethod
    def subtract(a, b):
        return a - b
    
# calling the static method
result = MathUtil.add(2, 3)
result2 = MathUtil.subtract(3, 2)
print(f"Result of {3} + {2} = {result}")
print(f"Result of {3} - {2} = {result2}")

# example 2

class KameDBZ:
    # static method allows you to call the method without creating an object
    @staticmethod
    def Kamehameha(power_level):
        print ("Kamehameha")
        return power_level * 10
    
goku_level= 900

damage_by_goku = KameDBZ.Kamehameha(goku_level)
print(f"Goku's power level is {goku_level} and he caused {damage_by_goku} damage")