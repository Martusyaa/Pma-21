from Figures.Figura import Figure
class Circle(Figure):
    def __init__(self,color,radius):
        if radius == 0:
            raise ValueError("Circle radius cannot be 0.")
        super().__init__(color)
        self.color = color
        self.radius = radius

    def perimetr(self):
        return 3.14 * self.radius

    def square(self):
        return 2 * 3.14 * self.radius * self.radius
