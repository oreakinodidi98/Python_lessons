# operators overloading

class Rectangle:

    def __init__(self, length, width) -> None:
        self.length = length
        self.width = width
    # with add you have a self and other
    def __add__(self, other):
        #rectangle 1 = self, rectangle 2 = other
        new_length = self.length + other.length
        new_width = self.width + other.width
        return Rectangle(new_length, new_width)
    
    def __str__(self) -> str:
        return f"Rectangle(Length:{self.length} Width:{self.width})"

rectangle1 = Rectangle(10, 20)
rectangle2 = Rectangle(20, 30)
# rectangle3 = rectangle1.__add__(rectangle2)
rectangle3 = rectangle1 + rectangle2
print(rectangle3)