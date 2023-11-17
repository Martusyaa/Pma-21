from abc import ABC,abstractmethod
class Color(ABC):
    @abstractmethod
    def fill_color(self):
        pass
