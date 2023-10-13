from abc import ABC, abstractmethod
ERROR = "Сторони мають бути більші за 0  "
ERROR1="Радіус має бути додатнім"
# Ієрархія 1
class Shape(ABC):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass

    @abstractmethod
    def name(self):
        pass

# Ієрархія 2
class Color(ABC):
    @abstractmethod
    def fill_color(self):
        pass

class RedColor(Color):
    def fill_color(self):
        return "Red"

class YellowColor(Color):
    def fill_color(self):
        return "Yellow"

class BlueColor(Color):
    def fill_color(self):
        return "Blue"

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        if radius <= 0:
            raise ValueError(ERROR1)
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius ** 2

    def calculate_perimeter(self):
        return 2 * 3.14 * self.radius

    def name(self):
        return 'Circle'

class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        if width <= 0 or height <= 0:
            raise ValueError(ERROR)
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

    def name(self):
        return 'Rectangle'

class Square(Shape):
    def __init__(self, color, side_length):
        super().__init__(color)
        if side_length <= 0:
            raise ValueError(ERROR)
        self.side_length = side_length

    def calculate_area(self):
        return self.side_length ** 2

    def calculate_perimeter(self):
        return 4 * self.side_length

    def name(self):
        return 'Square'

red_circle = Circle(RedColor(), 8)
yellow_rectangle = Rectangle(YellowColor(), 9, 9)
blue_square = Square(BlueColor(), 10)

print(f"{red_circle.name()} (Color: {red_circle.color.fill_color()}) - Area: {red_circle.calculate_area()}, Perimeter: {red_circle.calculate_perimeter()}")
print(f"{yellow_rectangle.name()} (Color: {yellow_rectangle.color.fill_color()}) - Area: {yellow_rectangle.calculate_area()}, Perimeter: {yellow_rectangle.calculate_perimeter()}")
print(f"{blue_square.name()} (Color: {blue_square.color.fill_color()}) - Area: {blue_square.calculate_area()}, Perimeter: {blue_square.calculate_perimeter()}")

