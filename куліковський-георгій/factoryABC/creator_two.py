from abstract_creator import Abstract_Creator
from product_two import Product_Two


class Creator_Two(Abstract_Creator):
    
    
    def create_product(self):
        return Product_Two()