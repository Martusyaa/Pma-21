from Figurs.Rectangle import Rectangle
from Figurs.Сircle import Circle
from Figurs.Square import Square
from Colors.Blue import Blue
from Colors.Green import Green
from Colors.Yellow import Yellow

if __name__ == '__main__':
    print("Коло:")
    try:
        Circle = Circle(Blue(), 3)
        Circle.print()
    except ValueError as e:
        print(e)

    print("Прямокутник:")
    try:
        Rectangle = Rectangle(Yellow(), 2, 5, 2, 3)
        Rectangle.print()
    except ValueError as e:
        print(e)

    print("Квадрат:")
    try:
        Square = Square(Green(), 2)
        Square.print()
    except ValueError as e:
        print(e)