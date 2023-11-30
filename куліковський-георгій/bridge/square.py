from rectangle import Rectangle


class Square(Rectangle):
    
    
    def __init__(self, value_one, color):
        if value_one >0:
            super().__init__(value_one, value_one, color)
        else:
            raise ValueError