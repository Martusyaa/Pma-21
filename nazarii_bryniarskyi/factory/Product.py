


class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.__class__.__name__}, name: {self.name}, price: {self.price}"


class Phone(Product):

    def __init__(self, name, price, number):
        super().__init__(name, price)
        self.number = number

    def call(self, other_number):
        print("Calling to ", other_number)

    def __str__(self):
        return super().__str__() + f", number: {self.number}"


class Monitor(Product):

    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size

    def __str__(self):
        return super().__str__() + f", size: {self.size}"
