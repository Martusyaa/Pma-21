def validator(func):
    def wrapper(self, a,scalar = None):
        if self.size != a.size or scalar == 0:
            raise ValueError("Vectors must have the same amount of values")
        return func(self, a)
    return wrapper