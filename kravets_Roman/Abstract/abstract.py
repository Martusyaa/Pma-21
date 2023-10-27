class Shape:
    def __init__(self, color):
        self.color = color
    def draw(self):
        pass
class Color:
    def fill_color(self):
        pass
class Red(Color):
    def fill_color(self):
        return "Red"
class Green(Color):
    def fill_color(self):
        return "Green"
class Blue(Color):
    def fill_color(self):
        return "Blue"
class Circle(Shape):
    def draw(self):
        return f"Circle drawn with {self.color.fill_color()} color."
    def calculate_area(self, radius):
        return 3.14 * radius * radius
    def calculate_perimeter(self, radius):
        return 2 * 3.14 * radius
class Rectangle(Shape):
    def draw(self):
        return f"Rectangle drawn with {self.color.fill_color()} color."

    def calculate_area(self, length, width):
        return length * width

    def calculate_perimeter(self, length, width):
        return 2 * (length + width)

class Square(Shape):
    def draw(self):
        return f"Square drawn with {self.color.fill_color()} color."
    def calculate_area(self, side):
        return side * side
    def calculate_perimeter(self, side):
        return 4 * side

if __name__ == "__main__":
    red_color = Red()
    green_color = Green()
    blue_color = Blue()
    circle = Circle(red_color)
    rectangle = Rectangle(green_color)
    square = Square(blue_color)
    print(circle.draw())
    print(f"Circle area: {circle.calculate_area(5)}")
    print(f"Circle perimeter: {circle.calculate_perimeter(5)}")
    print(rectangle.draw())
    print(f"Rectangle area: {rectangle.calculate_area(4, 6)}")
    print(f"Rectangle perimeter: {rectangle.calculate_perimeter(4, 6)}")
    print(square.draw())
    print(f"Square area: {square.calculate_area(3)}")
    print(f"Square perimeter: {square.calculate_perimeter(3)}")
