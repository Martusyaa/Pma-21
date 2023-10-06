from abstract_creator import Abstract_Creator
from product_one import Product_One


class Creator_One(Abstract_Creator):
    
    
    def create_product(self):
        return Product_One()