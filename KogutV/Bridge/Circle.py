from Shapes import *
from ShapeValidators import circle_validator
from math import pi

class Circle(Shape):
    def __init__(self, color,radius):
        super().__init__(color)
        self.radius = radius

    @circle_validator
    def calculate_area(self):
        return pi * self.radius ** 2
        
    @circle_validator
    def calculate_perimeter(self):
        return 2 * pi * self.radius