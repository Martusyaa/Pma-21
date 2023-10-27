from Figures.Figura import Figure
class Rectangle(Figure):
    def __init__(self,color,first_side,second_side):
        super().__init__(color)
        self.color = color
        self.first_side= first_side
        self.second_side = second_side

    def perimetr(self):
        if self.first_side is None or self.second_side is None:
            raise ValueError("Both sides must be provided to calculate the perimeter.")
        try:
            result = (self.first_side * self.second_side) * 2
        except ZeroDivisionError:
            result = "One or both sides are zero. Cannot calculate perimeter."
        except TypeError:
            result = "Invalid input. Make sure both sides are numeric."
        return result

    def square(self):
        return self.first_side * self.second_side
