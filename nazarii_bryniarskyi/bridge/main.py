from Color import Blue, Green, Red
from Shape import Circle, Square, Rectangle


def main():
    color_blue = Blue()
    color_green = Green()
    color_red = Red()

    shape_circle = Circle(color_blue, 3)
    shape_square = Square(color_green, 6)
    shape_rectangle = Rectangle(color_red, 4, 5)

    print(shape_circle)
    print(shape_square)
    print(shape_rectangle)


main()
