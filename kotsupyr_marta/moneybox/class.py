from main import MoneyBox

n = int(input("Введіть місткість скарбнички: "))
m = int(input("Скільки монет поклали в скарбничку: "))
k = int(input("Кількість монет, які хочуть покласти в скарбничку: "))
money_box = MoneyBox(n)
money_box.add(m)
result = money_box.can_add(k)
print(result)
