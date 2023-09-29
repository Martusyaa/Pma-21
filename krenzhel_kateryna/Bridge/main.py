from classes.figures.circle import Circle
from classes.figures.rectangle import Rectangle
from classes.figures.square import Square
from classes.figures.triangle import Triangle
from classes.colors.red import RedColor
from classes.colors.blue import BlueColor
from classes.colors.green import GreenColor

red_circle = Circle(RedColor(), 5)
red_circle.print()

green_rectangle = Rectangle(GreenColor(), 4, 6)
green_rectangle.print()

blue_square = Square(BlueColor(), 3)
blue_square.print()

red_triangle = Triangle(RedColor(), 3, 4, 5)
red_triangle.print()
