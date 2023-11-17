from Figure import Figure
import math
class Circle(Figure):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius


    def perimeter(self):
        if self.radius < 0:
            raise ValueError("Радіус не може бути від'ємним!")
        else:
            return round(2 * math.pi * self.radius, 2)

    def area(self):
        if self.radius < 0:
            raise ValueError("Радіус не може бути від'ємним!")
        else:
            return round(math.pi * self.radius * self.radius, 2)