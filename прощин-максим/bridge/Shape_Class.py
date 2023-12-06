from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, color):
        self.color = color

    def draw(self):
        pass

    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius, color):
        super().__init__(color)
        if radius < 0:
            raise ValueError("The radius cannot be less than zero")
        self.radius = radius

    def draw(self):
        return f"A {self.color} circle with radius {self.radius}"

    def calculate_area(self):
        return 3.14 * self.radius * self.radius

    def calculate_perimeter(self):
        return 2 * 3.14 * self.radius

class Rectangle(Shape):
    def __init__(self, width, height, color):
        super().__init__(color)
        if width < 0 or height < 0:
            raise ValueError("Width and height cannot be less than zero")
        self.width = width
        self.height = height

    def draw(self):
        return f"A {self.color} rectangle with width {self.width} and height {self.height}"

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

class Square(Rectangle):
    def __init__(self, side, color):
        if side < 0:
            raise ValueError("Side length must cannot be less than zero")
        super().__init__(side, side, color)

    def draw(self):
        return f"A {self.color} square with side {self.width}"