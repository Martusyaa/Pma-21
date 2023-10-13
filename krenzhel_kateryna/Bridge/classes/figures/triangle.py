from abc import ABC, abstractmethod
from classes.figures.figure import Figure
import math
ERROR = "Sides must be more than 0."

class Triangle(Figure):
    def __init__(self, color, first_side, second_side, third_side):
        super().__init__(color)
        try:
            if first_side <= 0 or second_side <= 0 or third_side <= 0:
                raise ValueError("Sides must be more than 0.")
            self.first_side = first_side
            self.second_side = second_side
            self.third_side = third_side
        except ValueError as e:
            print(f"Error: {e}")
            self.first_side = self.second_side = self.third_side = 0

    def calculate_perimeter(self):
        return self.first_side + self.second_side + self.third_side

    def name(self):
        return 'Triangle'

    def calculate_area(self):
        s = self.calculate_perimeter() / 2
        return math.sqrt(s * (s - self.first_side) * (s - self.second_side) * (s - self.third_side))
