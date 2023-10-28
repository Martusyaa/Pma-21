Fruits = {
    'Apple': {'Price': 30},
    'Orange': {'Price': 99},
    'Banana': {'Price': 50}
}
print("In start:")
for fruit, value in Fruits.items():
    print(f"Fruit: {fruit}, Price: {value['Price']}Uah")
print('\n')
Fruits.pop('Apple')
print("After deleting apple:")
for fruit, value in Fruits.items():
    print(f"Fruit: {fruit}, Price: {value['Price']}Uah")
print('\n')
Fruits.update({'Orange': {'Price': 109}})
print("After updating price of orange:")
for fruit, value in Fruits.items():
    print(f"Fruit: {fruit}, Price: {value['Price']}Uah")
print('\n')

