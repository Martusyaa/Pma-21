class Shape:
    def __init__(self, color):
        self.color = color

    def draw(self):
        pass

    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass

class Circle(Shape):
    def draw(self):
        return f"Draw a {self.color} circle"

    def calculate_area(self, radius):
        return 3.14 * radius * radius

    def calculate_perimeter(self, radius):
        return 2 * 3.14 * radius

class Rectangle(Shape):
    def draw(self):
        return f"Draw a {self.color} rectangle"

    def calculate_area(self, width, height):
        return width * height

    def calculate_perimeter(self, width, height):
        return 2 * (width + height)

class Square(Shape):
    def draw(self):
        return f"Draw a {self.color} square"

    def calculate_area(self, side):
        return side * side

    def calculate_perimeter(self, side):
        return 4 * side

class Color:
    def fill_color(self):
        pass

class RedColor(Color):
    def fill_color(self):
        return "Red"

class BlueColor(Color):
    def fill_color(self):
        return "Blue"

class GreenColor(Color):
    def fill_color(self):
        return "Green"

def main():
    shape_type = input("Виберіть фігуру (circle, rectangle, square): ").lower()
    color_type = input("Виберіть колір (red, blue, green): ").lower()

    if shape_type == "circle":
        color = eval(f"{color_type.capitalize()}Color()")
        radius = float(input("Введіть радіус: "))
        if radius >= 0:
            shape = Circle(color)
            print(shape.draw())
            print(f"Area: {shape.calculate_area(radius)}")
            print(f"Perimeter: {shape.calculate_perimeter(radius)}")
        else:
            print("Радіус не може бути від'ємним")
    elif shape_type == "rectangle":
        color = eval(f"{color_type.capitalize()}Color()")
        width = float(input("Введіть ширину: "))
        height = float(input("Введіть висоту: "))
        if width >= 0 and height >= 0:
            shape = Rectangle(color)
            print(shape.draw())
            print(f"Area: {shape.calculate_area(width, height)}")
            print(f"Perimeter: {shape.calculate_perimeter(width, height)}")
        else:
            print("Ширина і висота повинні бути додатними числами")
    elif shape_type == "square":
        color = eval(f"{color_type.capitalize()}Color()")
        side = float(input("Введіть довжину сторони: "))
        if side >= 0:
            shape = Square(color)
            print(shape.draw())
            print(f"Area: {shape.calculate_area(side)}")
            print(f"Perimeter: {shape.calculate_perimeter(side)}")
        else:
            print("Довжина сторони не може бути від'ємною")
    else:
        print("Невірний вибір фігури")

if __name__ == "__main__":
    main()
