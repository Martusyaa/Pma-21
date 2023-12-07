from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self,colour):
        self.colour = colour

    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass

    def display(self):
        print('Perimeter:', self.calculate_perimeter())
        print('Area:', self.calculate_area())
        print('Color:', self.colour.set_colour())