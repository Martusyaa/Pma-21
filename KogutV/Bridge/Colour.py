from abc import ABC,abstractmethod

class Colour(ABC):
    @abstractmethod
    def set_colour(self):
        pass