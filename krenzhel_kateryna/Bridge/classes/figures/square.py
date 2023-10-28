from classes.figures.figure import Figure
ERROR = "Sides must be more than 0."

class Square(Figure):
    def __init__(self, color, side):
        super().__init__(color)
        try:
            if side <= 0:
                raise ValueError(ERROR)
            self.side = side
        except ValueError as e:
            print(f"Error: {e}")
            self.side = 0

    def calculate_perimeter(self):
        return 4 * self.side

    def name(self):
        return 'Square'

    def calculate_area(self):
        return self.side * self.side