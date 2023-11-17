from abc import ABC, abstractmethod


class Shape(ABC):

    def __init__(self, color):
        self.color = color

    def getColor(self):
        return self.color

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def square(self):
        pass

    def __str__(self):
        return f"{self.__class__.__name__}: color: {self.color}, perimeter: {self.perimeter()}, square: {self.square()}"


class Circle(Shape):

    def __init__(self, color, side):
        super().__init__(color)
        self.color = color
        self.side = side

    def perimeter(self):
        return 2 * 3.14 * self.side

    def square(self):
        return 3.14 * self.side**2


class Rectangle(Shape):

    def __init__(self, color, side_a, side_b):
        super().__init__(color)
        self.color = color
        self.side_a = side_a
        self.side_b = side_b

    def perimeter(self):
        return 2 * (self.side_a + self.side_b)

    def square(self):
        return self.side_a * self.side_b


class Square(Rectangle):

    def __init__(self, color, side):
        super().__init__(color, side, side)
