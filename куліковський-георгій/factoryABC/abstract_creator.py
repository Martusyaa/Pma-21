from abc import ABC, abstractmethod


class Abstract_Creator(ABC):
    
    
    @abstractmethod
    def create_product(self):
        pass