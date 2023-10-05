from Product import Phone, Monitor

class Factory:

    @staticmethod
    def create(product_type, *parameter):
        if product_type == "Phone":
            return Phone(parameter[0], parameter[1], parameter[2])
        if product_type == "Monitor":
            return Monitor(parameter[0], parameter[1], parameter[2])
        else:
            return None
