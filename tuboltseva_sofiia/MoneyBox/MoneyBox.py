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

n = int(input("Місткість скарбнички: "))
money_box = MoneyBox(n)

try:
    m = int(input("Кількість монет, які поклали в скарбничку: "))
except ValueError:
    print("Помилка: Введене значення не є числом.")
    m = 0

money_box.coins = m

for i in range(m):
    money_box.add(1)

try:
    k = int(input("Кількість монет, які хочуть покласти в скарбничку: "))
except ValueError:
    print("Помилка: Введене значення не є числом.")
    k = 0
if money_box.can_add(k):
    print(False)
    money_box.add(k)
else:
    print(True)
