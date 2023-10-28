from abc import ABC, abstractmethod
import sys
import math
from color import *

class Shape(ABC):
    def __init__(self,color:Color):
        self.color = color

    @abstractmethod
    def square(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius,color:Color):
        super().__init__(color)
        self.radius = radius

    def square(self):
        if self.radius<0:
            raise Exception("Not valid value")
        else:
         return self.radius ** 2 * math.pi


    def perimeter(self):
            if self.radius<0:
                raise Exception("Not valid value")
            else:
                return self.radius * 2 * math.pi


    def __str__(self):
        return f"Shape: {self.__class__.__name__}, Radius: {self.radius}, Square: {self.square()}, Lenght: {self.perimeter()}, Color: {self.color}"



class Rectangle(Shape):
    def __init__(self, side_first, side_second,color:Color):
        super().__init__(color)
        self.side_first = side_first
        self.side_second = side_second

    def square(self):
        if self.side_first<=0 or self.side_second<=0:
            raise Exception("Not valid value")
        else:
            return self.side_first * self.side_second

    def perimeter(self):
        if self.side_first<=0 or self.side_second<=0:
            raise Exception("Not valid value")
        else:
            return 2 * (self.side_first + self.side_second)

    def __str__(self):
        return f"Shape: {self.__class__.__name__}, First side: {self.side_first}, Second side: {self.side_second},  Square: {self.square()}, Lenght: {self.perimeter()}, Color: {self.color} "



class Square(Rectangle):
    def __init__(self, side_first,color:Color):
        super().__init__(side_first, side_first,color)

    def square(self):
        if self.side_first<=0:
            raise Exception("Not valid value")
        else:
            return super().square()

    def perimeter(self):
        if self.side_first<=0:
            raise Exception("Not valid value")
        else:
            return super().perimeter()

    def __str__(self):
        return f"Shape: {self.__class__.__name__}, Side: {self.side_first}, Square: {self.square()}, Lenght: {self.perimeter()}, Color: {self.color} "

