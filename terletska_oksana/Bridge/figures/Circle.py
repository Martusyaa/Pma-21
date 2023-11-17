from figures.Shape import Shape
from math import pi


class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def name(self):
        return 'Circle'

    def area(self):
        if self.radius <= 0:
            raise ValueError('Радіус має бути > 0')
        else:
            return pi * self.radius ** 2

    def perimeter(self):
        if self.radius <= 0:
            raise ValueError('Радіус має бути > 0')
        else:
            return 2 * pi * self.radius
