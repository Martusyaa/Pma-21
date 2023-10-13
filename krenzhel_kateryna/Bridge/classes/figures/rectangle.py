from classes.figures.figure import Figure
ERROR = "Sides must be more than 0."

class Rectangle(Figure):
    def __init__(self, color, length, width):
        super().__init__(color)
        try:
            if length <= 0 or width <= 0:
                raise ValueError(ERROR)
            self.length = length
            self.width = width
        except ValueError as e:
            print(f"Error: {e}")
            self.length = self.width = 0

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

    def name(self):
        return 'Rectangle'

    def calculate_area(self):
        return self.length * self.width