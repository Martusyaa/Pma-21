from abc import ABC, abstractmethod
class Figure(ABC):
    def __init__(self, color):
        self.color = color


    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass

    def print(self):
        print('Периметр:', self.perimeter())
        print('Площа:', self.area())
        print('Колір:', self.color.Painting())
        print('-'*12)