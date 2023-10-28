class MoneyBox:
    def __init__(self,capacity):
        self.capacity = capacity
        self.coins = 0

    def can_add(self,v):
        return self.coins + v <= self.capacity

    def add(self,v):
        if self.can_add(v):
            self.coins += v
            return True
        else:
            return False
n = int(input("Enter capacity of MoneyBox"))
if n == 0:
    print("The money box does not exist")
else:
    m = int(input("the number of coins"))
    k = int(input("how much coins want to add"))

    money_box = MoneyBox(n)

    if money_box.add(m):
        result = money_box.add(k)
        print(result)






