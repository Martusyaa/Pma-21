from classes.figure.shape import Shape
ValueErrorOfSide = "Сторони мають бути більші за 0 "
class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        if width <= 0 or height <= 0:
            raise ValueError(ValueErrorOfSide)
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

    def name(self):
        return 'Rectangle'
