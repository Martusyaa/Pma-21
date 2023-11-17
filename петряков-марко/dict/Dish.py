class Dish:

    def __init__(self,price:int):
        self.price = price

    def __str__(self):
        return f"{self.price}"

