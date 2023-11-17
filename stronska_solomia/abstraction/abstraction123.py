class Figure:
    def __init__(self, color):
        self.color = color

    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass

class Circle(Figure):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius**2

    def calculate_perimeter(self):
        return 2 * 3.14 * self.radius


class Rectangle(Figure):
    def __init__(self, color, length, width):
        super().__init__(color)
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)


class Square(Rectangle):
    def __init__(self, color, side):
        super().__init__(color,side,side)
        self.side = side

    def calculate_area(self):
        return self.side**2

    def calculate_perimeter(self):
        return 4 * self.side


class Color:
    def apply_color(self):
        pass


class Red(Color):
    def apply_color(self):
        return "Red"


class Blue(Color):
    def apply_color(self):
        return "Blue"


class Green(Color):
    def apply_color(self):
        return "Green"

class ColoredShape:
    def __init__(self, shape, color):
        self.shape = shape
        self.color = color

    def display_info(self):
        print(f"Shape: {type(self.shape).__name__}, Color: {self.color.apply_color()}, "
              f"Area: {self.shape.calculate_area()}, Perimeter: {self.shape.calculate_perimeter()}")


user_choice = int(input("Enter 1 for Circle, 2 for Rectangle, 3 for Square: "))
length = float(input("Enter length: ")) if user_choice != 1 else 0
width = float(input("Enter width: ")) if user_choice == 2 else 0
radius = float(input("Enter radius: ")) if user_choice == 1 else 0

color_choice = int(input("Enter 1 for Red, 2 for Blue, 3 for Green: "))
colors = {1: Red(), 2: Blue(), 3: Green()}
selected_color = colors[color_choice]


if user_choice == 1:
    shape = Circle(selected_color, radius)
elif user_choice == 2:
    shape = Rectangle(selected_color, length, width)
elif user_choice == 3:
    shape = Square(selected_color, length)

colored_shape = ColoredShape(shape, selected_color)
colored_shape.display_info()