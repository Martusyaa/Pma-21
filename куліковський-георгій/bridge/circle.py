from shapes import Shapes
from math import pi


class Circle(Shapes):
    
    
    def __init__(self, value_one, color):
        if value_one >0:
            self.color = color
            self.value_one = value_one
        else:
            raise ValueError
        
        
    def perimeter(self):
        return round(2*pi*self.value_one,2)
    
    
    def area(self):
        return round(pi*self.value_one*self.value_one,2)
    
    
    def get_color(self):
        return str(self.color)
    
    
    def __str__(self):
        return f'Area: {self.area()}, Perimeter: {self.perimeter()}, Color: {self.get_color()}'
        
        
    