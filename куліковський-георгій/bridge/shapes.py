from abc import ABC, abstractmethod


class Shapes(ABC):
    
    
    @abstractmethod
    def area(self):
        pass
    
    
    @abstractmethod
    def perimeter(self):
        pass