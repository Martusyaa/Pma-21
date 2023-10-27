def Validator(method):
    def wrapper(self, amount):
        if self.assets + amount > self.assets_limit:
            raise ValueError("You can not add higher amount of assets than the limit")
        return method(self, amount)
    return wrapper
