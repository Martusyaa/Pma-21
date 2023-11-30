from abc import ABC, abstractmethod


class Abstract_Builder(ABC):
    
    
    @abstractmethod
    def product(self):
        pass
    
    
    @abstractmethod
    def add_part_a(self):
        pass
    
    
    @abstractmethod
    def add_part_b(self):
        pass
    
    
class Product:
    
    
    def __init__(self):
        self.parts = []
        
        
    def add(self, part):
        self.parts.append(part)
        
        
    def display(self):
        print(self.parts)
    

class Builder(Abstract_Builder):
    
    
    def __init__(self):
        self.reset()
        
        
    def reset(self):
        self._product = Product()
        
        
    def add_part_a(self):
        return self._product.add("Part A")
    
    
    def add_part_b(self):
        return self._product.add("Part B")
    
    
    def product(self):
        product = self._product
        self.reset()
        return product
    
    
class Director:
    
    
    def __init__(self):
        self._builder = None
        

    def set_builder(self, builder):
        self._builder = builder
        
    def builder(self):
        return self._builder
    
        
    def all_features(self):
        self._builder.add_part_a()
        self._builder.add_part_b()
        
