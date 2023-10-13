class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity
        self.coins = 0
    def can_add(self, v):
        return self.coins + v <= self.capacity
    def add(self, v):
        if self.can_add(v):
            self.coins += v
            return True
        else:
            return False



