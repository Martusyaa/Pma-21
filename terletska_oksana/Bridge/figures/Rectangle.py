from figures.Shape import Shape


class Rectangle(Shape):
    def __init__(self, color, side_a, side_b):
        super().__init__(color)
        self.side_a = side_a
        self.side_b = side_b

    def name(self):
        return 'Rectangle'

    def area(self):
        if self.side_a | self.side_b <= 0:
            raise ValueError('Сторони мають бути > 0')
        else:
            return 2 * (self.side_a + self.side_b)

    def perimeter(self):
        if self.side_a | self.side_b <= 0:
            raise ValueError('Сторони мають бути > 0')
        else:
            return self.side_a * self.side_b
