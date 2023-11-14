from Figures.Figura import Figure
class Square(Figure):
    def __init__(self,color,side):
        if side <= 0:
            raise ValueError("Side length must be greater than 0")

        super().__init__(color)
        self.color = color
        self.side = side

    def perimetr(self):
        return self.side * 4

    def square(self):
        return self.side * self.side