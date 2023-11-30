from MoneyBox import MoneyBox
if __name__ == '__main__':
    try:
        n = int(input("Місткість скарбнички: "))
        m = int(input("Скільки монет є в копілці: "))

        my_money_box = MoneyBox(n)

        for i in range(m):
            my_money_box.add(1)

        k = int(input("Кількість монет, які додаємо: "))

        result = my_money_box.can_add(k)

        print(result)
    except ValueError as e:
        print(f"Помилка: {e}. Введіть числове значення.")


