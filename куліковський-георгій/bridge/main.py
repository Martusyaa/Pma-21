from circle import Circle
from rectangle import Rectangle
from triangle import Triangle
from square import Square
from red import Red
from blue import Blue
from green import Green


def main():
    rect_one = Rectangle(10,20,Red())
    print(rect_one)
    square_one = Square(10,Blue())
    print(square_one)
    circle_one = Circle(10,Green())
    print(circle_one)
    triangle_one = Triangle(10,11,12,Red())
    print(triangle_one)
    
    
main()