def print_car(cars):
    for car, info in cars.items():
        print(f"Model: {car}, Price: ${info['Price']}, Year: {info['Year']}, Color: {info['Color']}")
    print('\n')
cars = {
    'Toyota Camry': {'Price': 25000, 'Year': 2023, 'Color': 'Silver'},
    'Honda Civic': {'Price': 22000, 'Year': 2023, 'Color': 'Blue'},
    'Ford Mustang': {'Price': 45000, 'Year': 2023, 'Color': 'Red'}
}

print_car(cars)
try:
    cars.pop('Toyota Camry')
except KeyError:
    print("No such key exists")

print("After removing Toyota Camry:")
print_car(cars)

cars['Honda Civic']['Price'] = 23000
print("After updating the Honda Civic price:")
print_car(cars)