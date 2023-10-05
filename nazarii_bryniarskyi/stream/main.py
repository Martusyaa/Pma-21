from Product import Product

def main():
    products = [Product("Apple", 2), Product("Potato"), Product("Izum🤮🤮", -3)]
    print("Old product prices")
    for i in range(len(products)):
        print(products[i], end='; ')

    products = list(map(lambda product: Product(product.product_name, product.price + 1), products))
    print("\n\nNew product prices")
    for i in range(len(products)):
        print(products[i], end='; ')


main()
