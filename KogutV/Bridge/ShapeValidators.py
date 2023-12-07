def rectangle_validator(method):
    def wrapper(self):
        if self.length <= 0 or self.width <= 0:
            raise ValueError("Both sides must be more than zero")
        return method(self)
    return wrapper

def square_validator(method):
    def wrapper(self):
        if self.side <= 0:
            raise ValueError("Side must be more than zero")
        return method(self)
    return wrapper

def circle_validator(method):
    def wrapper(self):
        if self.radius <= 0:
            raise ValueError("Radius must be more than zero")
        return method(self)
    return wrapper