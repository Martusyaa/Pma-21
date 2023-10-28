from figures.Rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, color, side):
        super().__init__(color, side, side)
        # self.side = side

    def name(self):
        return 'Square'

    def area(self):
        if self.side_a <= 0:
            raise ValueError('Сторона має бути > 0')
        else:
            return self.side_a ** 2

    def perimeter(self):
        if self.side_a <= 0:
            raise ValueError('Сторона має бути > 0')
        else:
            return 4 * self.side_a
