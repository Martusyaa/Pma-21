from Figures.Rectangle import Rectangle
from Figures.Circle import Circle
from Figures.Square import Square
from Colorss.Red import Red
from Colorss.Brown import Brown
from Colorss.Green import Green

def main():
    red_color = Red()
    green_color = Green()
    brown_color = Brown()

    try:
        figure_circle = Circle(red_color, 0)
    except ValueError:
        print("Error: Invalid input. Make sure to provide color and a non-zero radius for the circle.")
    else:
        print("Circle:")
        print(figure_circle)

    try:
        figure_square = Square(green_color, -7)
    except ValueError:
        print("Error: Invalid input. Make sure to provide color and a non-zero or negative side length for the square.")
    else:
        print("Square:")
        print(figure_square)
    try:
        figure_rectangle = Rectangle(brown_color, 5, 4)
    except TypeError:
        print("Error: Invalid input. Make sure to provide color, length, and width for the rectangle.")
    else:
        print("Rectangle:")
        print(figure_rectangle)


main()