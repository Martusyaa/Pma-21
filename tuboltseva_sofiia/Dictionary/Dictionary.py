class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"Name: {self.name}, Price$: {self.price}, Quantity: {self.quantity}"

Products = {
    "Product 1": Product("Ноутбук", 1000, 10),
    "Product 2": Product("Смартфон", 500, 20),
    "Product 3": Product("Планшет", 300, 15)
}

print("Початковий словник:","---"* 10)
for key in Products:
    print(key, Products[key])

print("Словник після видалення елементу:","--"*8)
key = "Product 3"
try:
    del Products[key]
except KeyError:
    print(f"Ключ '{key}' не знайдено в словнику.")
else:
    for key in Products:
        print(key, Products[key])

print("Словник після заміни товару:","--"*11)
new_item = Product("Комп'ютер", 1200, 5)
key = 'Product 2'
if key in Products:
    Products[key] = new_item
    for key in Products:
        print(key, Products[key])
else:
    print(f"Помилка: Ключ '{key}' не знайдено в словнику.")

print("Спроба доступу до неіснуючого ключа:","--"*7)
non_existent_key = 'Product 4 '
try:
    product = Products[non_existent_key]
except KeyError:
    print(f"Ключ  '{non_existent_key}'  не знайдено в словнику.")
else:
    print(product)
