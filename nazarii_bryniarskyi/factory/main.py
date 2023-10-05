from Factory import Factory


def main():
    product_phone = Factory.create("Phone", "Iphone", 999, "380965276291")
    product_monitor = Factory.create("Monitor", "Acer", 999, 17)
    product_unknown = Factory.create("kjenke")

    print(product_phone)
    print(product_monitor)
    print(product_unknown)


main()
