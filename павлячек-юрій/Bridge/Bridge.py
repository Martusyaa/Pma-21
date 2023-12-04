from Color import Blue, Red, Yellow
from Shape import Square, Rectangle, Circle

color_blue = Blue()
color_yellow = Yellow()
color_red = Red()

shape_square = Square(color_yellow, 2)
shape_rectangle = Rectangle(color_red, 2, 3)
shape_circle = Circle(color_blue, 4)

print(shape_square)
print(shape_rectangle)
print(shape_circle)
