from Shape_Class import Circle, Rectangle, Square
from Color_Class import RedColor, BlueColor, GreenColor

try:
    shape = Circle(5, RedColor())
    print(f"{shape.draw()}\nArea: {shape.calculate_area()}, Perimeter: {shape.calculate_perimeter()}\n")
except ValueError as e:
    print(f"Error(Circle): {e}\n")

try:
    shape = Rectangle(-4, 6, GreenColor())
    print(f"{shape.draw()}\nArea: {shape.calculate_area()}, Perimeter: {shape.calculate_perimeter()}\n")
except ValueError as e:
    print(f"Error(Rectangle): {e}\n")

try:
    shape = Square(5, BlueColor())
    print(f"{shape.draw()}\nArea: {shape.calculate_area()}, Perimeter: {shape.calculate_perimeter()}\n")
except ValueError as e:
    print(f"Error(Square): {e}\n")