from Shapes import *
from ShapeValidators import rectangle_validator

class Rectangle(Shape):
    def __init__(self, color,length,width):
        super().__init__(color)
        self.width = width
        self.length = length

    @rectangle_validator
    def calculate_area(self):
        return self.width * self.length
        
    @rectangle_validator
    def calculate_perimeter(self):
        return (self.width + self.length)*2