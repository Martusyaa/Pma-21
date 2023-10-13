from money_box import Money_Box


def main():
    money_box = Money_Box(400)
    money_box.add_coin(100)
    print(money_box)
    money_box.add_coin(500)


main()