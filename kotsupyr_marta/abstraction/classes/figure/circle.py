from classes.figure.shape import Shape
ValueErrorOfRadius="Радіус має бути додатнім"
class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        if radius <= 0:
            raise ValueError(ValueErrorOfRadius)
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius ** 2

    def calculate_perimeter(self):
        return 2 * 3.14 * self.radius

    def name(self):
        return 'Circle'
