from abc import ABC, abstractmethod
class Figure(ABC):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def calculate_perimeter(self):
        pass

    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def calculate_area(self):
        pass

    def print(self):
        print('Name:', self.name())
        print('Perimeter:', self.calculate_perimeter())
        print('Area:', self.calculate_area())
        print('Color:', self.color.apply_color())
        print('\n')

