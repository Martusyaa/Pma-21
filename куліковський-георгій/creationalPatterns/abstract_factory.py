from abc import ABC, abstractmethod


class Creator(ABC):
    
    
    @abstractmethod
    def create_product_A(self):
        pass
    
    
    @abstractmethod
    def create_product_B(self):
        pass
    

class Product_A(ABC):
    
    
    @abstractmethod
    def product_method(self):
        pass
    
    
class Product_B(ABC):
    
    
    @abstractmethod
    def product_method(self):
        pass
    

class Product_One_A(Product_A):
    
    
    def product_method(self):
        return "Product One A"
    
    
class Product_One_B(Product_B):
    
    
    def product_method(self):
        return "Product One B"

    
class Factory_One(Creator):
    
    
    def create_product_A(self):
        return Product_One_A()
    
    
    def create_product_B(self):
        return Product_One_B()
    
    
prodB = Factory_One().create_product_A()
prodA = Factory_One().create_product_B()
print(prodA.product_method(), prodB.product_method())