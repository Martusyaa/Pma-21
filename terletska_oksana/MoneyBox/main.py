class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity
        self.number_of_coins = 0

    def can_add(self, v):
        return self.number_of_coins + v <= self.capacity

    def add(self, v):
        if self.can_add(v):
            self.number_of_coins += v
            return True
        else:
          return False

try:
    n = int(input("Enter coin capacity: "))
    m = int(input("Enter number added coins: "))

    money_box = MoneyBox(n)

    for i in range(m):
        money_box.add(1)

    print("Can add more (True/False):")
    k = int(input("Number of coins, who want to put in money box: "))
    if k<0:
        raise ValueError("The number of coins can not be negative")
    result = money_box.add(k)
    print(result)
except ValueError as e:
    print(f"Error: {e}")
