from classes.figure.square import Square
from classes.figure.circle import Circle
from classes.figure.rectangle import Rectangle
from classes.color.red import RedColor
from classes.color.blue import BlueColor
from classes.color.yellow import YellowColor

red_circle = Circle(RedColor(), 8)
yellow_rectangle = Rectangle(YellowColor(), 9, 9)
blue_square = Square(BlueColor(), 10)

print(f"{red_circle.name()} (Color: {red_circle.color.fill_color()}) - Area: {red_circle.calculate_area()}, Perimeter: {red_circle.calculate_perimeter()}")
print(f"{yellow_rectangle.name()} (Color: {yellow_rectangle.color.fill_color()}) - Area: {yellow_rectangle.calculate_area()}, Perimeter: {yellow_rectangle.calculate_perimeter()}")
print(f"{blue_square.name()} (Color: {blue_square.color.fill_color()}) - Area: {blue_square.calculate_area()}, Perimeter: {blue_square.calculate_perimeter()}")

