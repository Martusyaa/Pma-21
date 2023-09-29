from classes.figures.figure import Figure
import math
ERROR = "Sides must be more than 0."

class Circle(Figure):
    def __init__(self, color, radius):
        super().__init__(color)
        try:
            if radius <= 0:
                raise ValueError(ERROR)
            self.radius = radius
        except ValueError as e:
            print(f"Error: {e}")
            self.radius = 0

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius

    def name(self):
        return 'Circle'

    def calculate_area(self):
        return math.pi * self.radius * self.radius