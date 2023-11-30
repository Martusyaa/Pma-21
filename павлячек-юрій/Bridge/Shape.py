from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return f"Class: {self.__class__.__name__}: color: {self.color}, perimeter: {self.perimeter()}, area: {self.area()}"

    def getColor(self):
        return self.color

    def perimeter(self):
        pass

    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, color, side_a, side_b):
        super().__init__(color)
        if side_a < 0 or side_b < 0:
            raise ValueError("Side must be positive")
        self.side_a = side_a
        self.side_b = side_b

    def perimeter(self):
        return (self.side_a + self.side_b) * 2

    def area(self):
        return self.side_a * self.side_b


class Square(Rectangle):
    def __init__(self, color, side):
        super().__init__(color, side, side)
        if side < 0:
            raise ValueError("Side must be positive")
        self.side = side


class Circle(Shape):
    def __init__(self, color, radius):
        if radius < 0:
            raise ValueError("side must be positive")
        super().__init__(color)
        self.radius = radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

    def area(self):
        return 3.14 * self.radius ** 2
