from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def print(self):
        print('\n')
        print('Name:', self.name())
        print('Perimeter:', self.perimeter())
        print('Area:', self.area())
        print('Color:', self.color.draw())
