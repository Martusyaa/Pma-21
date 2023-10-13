from MoneyBox import MoneyBox

def main():
    box = MoneyBox(10)
    box.add(6)
    print(box.can_add(5))
    print(box.can_add(-1))
    print(box.can_add(4))
    box.add(1000)


main()
