from abc import ABC, abstractmethod


class Color(ABC):
    
    
    @abstractmethod
    def __str__(self):
        pass