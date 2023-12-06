def capacity_agregator(func):
    def wrapper(self, *args, **kwargs):
        if self.size == self.capacity:
            self._increase_capacity()
        return func(self, *args, **kwargs)
    return wrapper