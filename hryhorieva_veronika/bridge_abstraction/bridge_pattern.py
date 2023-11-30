from abc import abstractmethod, ABC
import math
from color import *
import sys


class Shape(ABC):
    def __init__(self, color: Color):
        self.color = color

    @abstractmethod
    def square_count(self):
        pass

    @abstractmethod
    def perimetr_count(self):
        pass


class Circle(Shape):
    def __init__(self, radius: float, color: Color):
        super().__init__(color)
        try:
            self.radius = radius
            assert self.radius > 0
        except AssertionError:
            print("The negative number as the sides of Circle added")

    @property
    def square_count(self):
        return round(math.pi * self.radius ** 2, 3)

    def perimetr_count(self):
        return round(2 * math.pi * self.radius, 3)

    def __str__(self):
        return f' Color is: {self.color.print_color()}\nObject is: {self.__class__.__name__}, Square is: {self.square_count}, Perimetr is: {self.perimetr_count()}'


class Rectangle(Shape):
    def __init__(self, side_A: float, side_B: float, color: Color):
        super().__init__(color)
        try:
            self.side_A = side_A
            self.side_B = side_B
            assert self.side_B > 0 and self.side_A > 0
        except AssertionError as b:
            print(f"The negative number as the sides of {self.__class__.__name__} added")

    def square_count(self):
        return self.side_A * self.side_B

    def perimetr_count(self):
        return 2 * (self.side_A + self.side_B)

    def __str__(self):
        return f' Color is: {self.color.print_color()}\nObject is: {self.__class__.__name__}, Square is: {self.square_count()}, Perimetr is: {self.perimetr_count()}'


class Square(Rectangle):
    def __init__(self, side: float, color: Color):
        self.side=side
        super().__init__(side_A=side, side_B=side, color=color)



    def square_count(self):
        return self.side**2

    def perimetr_count(self):
        return 4 * self.side

    def __str__(self):
        return f' Color is: {self.color.print_color()}\nObject is: {self.__class__.__name__}, Square is: {self.square_count()}, Perimetr is: {self.perimetr_count()}'
