

class Product:

    def __init__(self, product_name, price=0):
        self.product_name = product_name
        self.price = price

    def __str__(self):
        return f"Product name: {self.product_name}, Price: {self.price}"
