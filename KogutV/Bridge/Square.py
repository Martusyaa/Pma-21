from Rectangle import *
from ShapeValidators import square_validator

class Square(Rectangle):
    def __init__(self, color,side):
        super().__init__(color,side,side)
        self.side = side

    @square_validator
    def calculate_area(self):
        return self.side ** 2
        
    @square_validator
    def calculate_perimeter(self):
        return self.side * 4