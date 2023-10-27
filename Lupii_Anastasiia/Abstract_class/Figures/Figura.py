from abc import ABC, abstractmethod


class Figure(ABC):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def square(self):
        pass

    @abstractmethod
    def perimetr(self):
        pass

    def __str__(self):
        return f"{self.__class__.__name__}: color: {self.color}, perimetr: {self.perimetr()}, square: {self.square()}"
