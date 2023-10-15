class MoneyBox:
    def __init__(self, capacity: int, v: int, filled_with=0, ):
        self.capacity = capacity
        self.filled_with = filled_with

    def __str__(self):
        return f"Coins inside money box: {self.filled_with}\nMax_coins: {self.capacity}"

    def can_add(self, amount: int):
        return self.filled_with + amount <= self.capacity

    def add(self, amount: int):
        try:
            if amount < 0:
                raise Exception("Amount of added coins lower than zero")
        except Exception as e:
            print(e)
            return

        if self.can_add(amount):
            self.filled_with += amount


a = MoneyBox(100, 10)
print(a)
a.add(100)
print(a)
a.add(12)
