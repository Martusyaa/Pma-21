from abc import ABC, abstractmethod


class Creator(ABC):
    
    
    @abstractmethod
    def create_product(self):
        pass
    

class Product(ABC):
    
    
    @abstractmethod
    def product_method(self):
        pass
    

class Product_One(Product):
    
    
    def product_method(self):
        return "Product One"

    
class Factory_One(Creator):
    
    
    def create_product(self):
        return Product_One()
    
    
p = Factory_One().create_product()
print(p.product_method())