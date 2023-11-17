from colors.colorWhite import White
from colors.colorBlue import Blue
from colors.colorPink import Pink

from figures.Rectangle import Rectangle
from figures.Square import Square
from figures.Circle import Circle

white_circle = Circle(White(), 5)
white_circle.print()

blue_rectangle = Rectangle(Blue(), 4, 6)
blue_rectangle.print()

pink_square = Square(Pink(), 3)
pink_square.print()
