import math
class Shape:
    def __init__(self, color):
        self.color = color

    def area(self):
        pass

    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def area(self):
        if self.radius <= 0:
            print("Радіус не може дорівнювати 0 чи бути меншою за 1!")
        else:
            return math.pi * self.radius * self.radius

    def perimeter(self):
        if self.radius <= 0:
            print("Радіус не може дорівнювати 0 чи бути меншою за 1!")
        else:
            return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height

    def area(self):
        if self.width <= 0 or self.height <= 0:
            print("Ширина та висота не може дорівнювати 0 чи бути меншою за 1!")
        else:
            return self.width * self.height

    def perimeter(self):
        if self.width <= 0 or self.height <= 0:
            print("Ширина та висота не може дорівнювати 0 чи бути меншою за 1!")
        else:
            return 2 * (self.width + self.height)

class Square(Shape):
    def __init__(self, color, side_length):
        super().__init__(color)
        self.side_length = side_length

    def area(self):
        if self.side_length <= 0:
            print("Ширина та висота не може дорівнювати 0 чи бути меншою за 1!")
        else:
        return self.side_length**2

    def perimeter(self):
        if self.side_length <= 0:
            print("Ширина та висота не може дорівнювати 0 чи бути меншою за 1!")
        else:
            return 4 * self.side_length

class Color:
    def apply_color(self):
        pass

class RedColor(Color):
    def apply_color(self, shape):
        return f"Red {shape.__class__.__name__}"

class GreenColor(Color):
    def apply_color(self, shape):
        return f"Green {shape.__class__.__name__}"

class BlueColor(Color):
    def apply_color(self, shape):
        return f"Blue {shape.__class__.__name__}"

red_circle = Circle(RedColor(), -1)
green_rectangle = Rectangle(GreenColor(), 3, 4)
blue_square = Square(BlueColor(), 2)

print(red_circle.area(), red_circle.perimeter(), red_circle.color.apply_color(red_circle))
print(green_rectangle.area(), green_rectangle.perimeter(), green_rectangle.color.apply_color(green_rectangle))
print(blue_square.area(), blue_square.perimeter(), blue_square.color.apply_color(blue_square))
