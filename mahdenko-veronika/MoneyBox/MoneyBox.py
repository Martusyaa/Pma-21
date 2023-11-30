class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity
        self.count_coins = 0

    def can_add(self, v):
        added = self.count_coins + v <= self.capacity
        return added

    def add(self, v):
        if self.can_add(v):
            self.count_coins += v
            return True
        else:
            return False