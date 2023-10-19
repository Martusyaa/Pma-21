from shapes import Shapes


class Rectangle(Shapes):
    
    def __init__(self, value_one, value_two, color):
        if value_one and value_two >0:
            self.value_two = value_two
            self.value_one = value_one
            self.color = color
        else:
            raise ValueError
            
        
    def area(self):
        return self.value_one * self.value_two
    
    
    def perimeter(self):
        return self.value_one*2 + self.value_two*2
    
    
    def get_color(self):
        return str(self.color)
    
    
    def __str__(self):
        return f'Area: {self.area()}, Perimeter: {self.perimeter()}, Color: {self.get_color()}'
    