from abc import abstractmethod, ABC
from math import pi
from color import *


class Figure(ABC):

    def __init__(self, color: Color):
        self.color = color

    def perimeter(self):
        pass

    def square(self):
        pass


class Circle(Figure):
    def __init__(self, radius: float, color: Color):
        super().__init__(color=color)
        self.radius = radius
        try:
            if self.radius < 0:
                self.radius = 0
                raise Exception("Lower than zero")
        except Exception as e:
            print(e)

    def calc_square(self) -> float:
        return pi * self.radius ** 2

    def calc_perimeter(self):
        return 2 * pi * self.radius

    def __str__(self):
        name = self.__class__.__name__
        return f"Object: {name} | Color: {self.color} \n" \
               f"Square: {round(self.calc_square(), 2)} | Perimeter: {round(self.calc_perimeter(), 2)}\n"


class Rectangle(Figure):
    def __init__(self, color: Color, sideA, sideB):
        super().__init__(color)
        self.sideA = sideA
        self.sideB = sideB
        try:
            if self.sideA < 0:
                self.sideA = 0
                raise Exception("SideA lower than zero")
            if self.sideB < 0:
                self.sideB = 0
                raise Exception("SideB lower than zero")
        except Exception as e:
            print(e)
            return

    def calc_square(self) -> float:
        return self.sideA * self.sideB

    def calc_perimeter(self):
        return 2 * (self.sideA + self.sideB)

    def __str__(self):
        name = self.__class__.__name__
        return f"Object: {name} Color: {self.color} \n" f"Sides A & B: {self.sideA, self.sideB} " \
               f"Square: {self.calc_square()} Perimeter: {self.calc_perimeter()}\n"


class Square(Rectangle):
    def __init__(self, side: float, color: Color):
        super().__init__(color=color, sideA=side, sideB=side)

    def calc_square(self) -> float:
        return self.sideA ** 2

    def calc_perimeter(self):
        return 4 * self.sideA

    def __str__(self):
        name = self.__class__.__name__
        return f"Object: {name} Color: {self.color} \n" \
               f"Square: {self.calc_square()} Perimeter: {self.calc_perimeter()}\n"
