class Figure:
    def __init__(self, color):
        self.color = color
        self.validate_color()

    def validate_color(self):
        allowed_colors = {'Red', 'Green', 'Blue'}
        if not isinstance(self.color, Color) or self.color.apply_color() not in allowed_colors:
            raise ValueError(" Недопустимий колір")

    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass


class Circle(Figure):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius ** 2

    def calculate_perimeter(self):
        return 2 * 3.14 * self.radius


class Rectangle(Figure):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)


class Square(Figure):
    def __init__(self, color, side_length):
        super().__init__(color)
        self.side_length = side_length

    def calculate_area(self):
        return self.side_length ** 2

    def calculate_perimeter(self):
        return 4 * self.side_length


class Color:
    def apply_color(self):
        return "No Color"


class RedColor(Color):
    def apply_color(self):
        return "Red"


class GreenColor(Color):
    def apply_color(self):
        return "Green"


class BlueColor(Color):
    def apply_color(self):
        return "Blue"


try:
    red_circle = Circle(RedColor(), 5)
    print(f"Circle: Color: {red_circle.color.apply_color()}, Area: {red_circle.calculate_area()}")

    green_rectangle = Rectangle(GreenColor(), 4, 6)
    print(f"Rectangle: Color: {green_rectangle.color.apply_color()}, Perimeter: {green_rectangle.calculate_perimeter()}")

    blue_square = Square(BlueColor(), 3)
    print(f"Square: Color: {blue_square.color.apply_color()}, Area: {blue_square.calculate_area()}")

    gray_square = Square("gray", 2)
    print(f"Square: Color: {gray_square.color.apply_color()}, Area: {gray_square.calculate_area()}")

except ValueError as e:
    print(f"Помилка: {e}")
