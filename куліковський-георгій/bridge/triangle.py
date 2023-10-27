from shapes import Shapes


class Triangle(Shapes):
    
    def __init__(self, value_one, value_two, value_three, color):
        if value_one and value_two and value_three >0:
            self.value_one = value_one
            self.value_two = value_two
            self.value_three = value_three
            self.color = color
        else:
            raise ValueError
      
      
    def perimeter(self):
        return self.value_one + self.value_two + self.value_three
      
        
    def area(self):
        return round(((self.perimeter()/2) * (self.perimeter()/2 - self.value_one)\
            * (self.perimeter()/2 - self.value_two) * (self.perimeter()/2 - self.value_three))**1/2,2)
        
        
    def get_color(self):
        return self.color
        
        
    def __str__(self):
        return f'Area: {self.area()}, Perimeter: {self.perimeter()}, Color: {self.color}'