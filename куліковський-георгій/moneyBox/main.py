from money_box import Money_Box


def main():
    money_box = Money_Box(400, 200)
    money_box.add_coin()
    print(money_box)
    money_box.add_amount(100)
    print(money_box)
    print(money_box.can_add(2000))
    money_box.add_amount(2000)


main()