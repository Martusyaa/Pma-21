from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass

class Color(ABC):
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color


class Circle(Shape):
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("The radius must be non-negative")
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius ** 2

    def calculate_perimeter(self):
        return 2 * 3.14 * self.radius

    def __str__(self):
        return "Circle"


class Rectangle(Shape):
    def __init__(self, height, width):
        if height < 0 or width < 0:
            raise ValueError("The height and width must be non-negative")
        self.height = height
        self.width = width

    def calculate_perimeter(self):
        return self.height * 2 + self.width * 2

    def calculate_area(self):
        return self.width * self.height

    def __str__(self):
        return "Rectangle"


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def __str__(self):
        return "Square"

class Purple(Color):
        def __init__(self):
            super().__init__('Purple')

class Blue(Color):
        def __init__(self):
            super().__init__('Blue')

class Yellow(Color):
        def __init__(self):
            super().__init__('Yellow')

class Bridge:
    def __init__(self, shape, color):
        self.shape = shape
        self.color = color

    def info(self):
        return f"{self.color.get_color()} {self.shape} [Area = {self.shape.calculate_area()} Perimeter = {self.shape.calculate_perimeter()}]"

try:
    square = Square(5)
    blue = Blue()
    blue_square = Bridge(square, blue)
    print(blue_square.info())
except ValueError as e:
    print(f"Error: {e}")

try:
    rectangle = Rectangle(4, 6)
    purple = Purple()
    purple_rectangle = Bridge(rectangle, purple)
    print(purple_rectangle.info())
except ValueError as e:
    print(f"Error: {e}")

try:
    circle = Circle(-5)
    yellow = Yellow()
    circle_yellow = Bridge(circle, yellow)
    print(circle_yellow.info())
except ValueError as e:
    print(f"Error: {e}")