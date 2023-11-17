from abstract import *
from color import *


circle = Circle(-18, Red())

rectangle = Rectangle(3,4, Gold())
square = Square(4, Black())

try:
    print(circle)
except Exception as e:
    print(e)
print("-----------------------")
try:
    print(rectangle)
except Exception as e:
    print(e)
print("-----------------------")
try:
    print(square)
except Exception as e:
    print(e)