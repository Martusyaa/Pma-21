from classes.figure.shape import Shape
ValueErrorOfSide = "Сторони мають бути більші за 0 "
class Square(Shape):
    def __init__(self, color, side_length):
        super().__init__(color)
        if side_length <= 0:
            raise ValueError(ValueErrorOfSide)
        self.side_length = side_length

    def calculate_area(self):
        return self.side_length ** 2

    def calculate_perimeter(self):
        return 4 * self.side_length

    def name(self):
        return 'Square'
