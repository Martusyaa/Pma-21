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
# Вже після цього можна завершувати код, але я ще хочу дещо урізноманітнити його, тому
    #ще написав такі функції (методи), як : 1) Отримати поточний баланс скарбнички
    #                                       2) Вивести інформацію про скарбничку
    #                                       3) Видати гроші з скарбнички, якщо можливо
    def get_balance(self):
        return self.coins

    def print_info(self):
        print(f"Місткість скарбнички: {self.capacity}")
        print(f"Поточна кількість монет: {self.coins}")

    def withdraw(self, v):
        if self.coins >= v:
            self.coins -= v
            return True
        else:
            return False

n = int(input("Введіть місткість скарбнички: "))
money_box = MoneyBox(n)
m = int(input("Скільки монет поклали в скарбничку: "))
money_box.coins = m
k = int(input("Кількість монет, які хочуть покласти в скарбничку: "))
if money_box.can_add(k):
    result = money_box.add(k)
    print(result)
else:
    print(False)
money_box.print_info()
withdraw_amount = int(input("Скільки монет ви хочете видати?: "))
if money_box.withdraw(withdraw_amount):
    print("Видано гроші.")
else:
    print("Недостатньо грошей для видання.")
money_box.print_info()
