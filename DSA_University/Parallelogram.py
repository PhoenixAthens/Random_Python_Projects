import math
class Parallelogram:
    def __init__(self, length:int, breadth:int):
        self.side1:int=length
        self.side2:int=breadth

    def Perimeter(self)->float:
        return 2* ( self.side2+self.side1 )
    def Area(self)-> float:
        return self.side2*self.side1

class Rectangle(Parallelogram):
    def __init__(self, length, breadth):
        super().__init__(length,breadth)

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side,side)

class RightTriangle(Rectangle):
    def __init__(self, base, height):
        super().__init__(base, height)

    def Area(self) -> float:
        return 1/2*super().Area()

    def calcHypotenuse(self) -> float:
        return math.sqrt(math.pow(self.side1,2)+math.pow(self.side2,2))

    def Perimeter(self) -> float:
        return self.side1+self.side2+self.calcHypotenuse()

triangle1:RightTriangle = RightTriangle(3,4)
print(triangle1.Area())
print(triangle1.calcHypotenuse())
print(triangle1.Perimeter())

rectangle1: Rectangle = RightTriangle(3,4)   # this is fine, because RightTriangle is a Rectangle, but not the other way around
                                             # however because variable is of type Rectangle, we cannot access Triangle
                                             # specific method.
triangle2:RightTriangle = Rectangle(120,240) # This raises an error


