from Rectangle import Rectangle
from Сircle import Circle
from Square import Square
from Blue import Blue
from Green import Green
from Yellow import Yellow

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