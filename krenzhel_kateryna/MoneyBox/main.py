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

n = int(input("Input capacity:"))
m = int(input("Input numbers of coins which are added:"))
k = int(input("Input numbers of coins which are wanted to add:"))

money_box = MoneyBox(n)
result = money_box.add(m + k)
print(result)





