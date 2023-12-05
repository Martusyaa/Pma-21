cars = {
    'Toyota': 'Camry',
    'Honda': 'Civic',
    'Ford': 'Mustang',
    'Opel': 'Combo',
    'Citroen': 'Picaso',
}


def get_car(car):
    if cars.get(car) is None:
        raise KeyError
    else:
        return cars.get(car)


def delete_item(car):
    if cars.get(car) is None:
        raise KeyError
    else:
        cars.pop(car)
        return cars


print("Dictionary:", end=f' {cars}\n\n')

try:
    print("Get value by key 'Toyota':", end=f'{get_car("Toyota")}\n')
except KeyError:
    print("\tError: There is no such key in the dictionary")

try:
    print("Get value by key 'Mercedes':", end=f'{get_car("Mercedes")}\n\n')
except KeyError:
    print("\tError: There is no such key in the dictionary\n")

cars.update({'Mercedes': 'Sprinter'})
print("Add Mercedes to dictionary:", end=f'\n{cars}\n\n')

cars.update({'Honda': 'Accord'})
print("Update Honda cars from Civic to Accord:", end=f'\n{cars}\n\n')

try:
    if cars.get('Mercedes') is None:
        raise KeyError
    else:
        cars.pop('Mercedes')
        print("Remove Mercedes from dictionary:", end=f'\n{cars}\n\n')
except KeyError:
    print("\tError: There is no such key in the dictionary\n")

cars.pop('Citroen')
print("Remove Citroen from dictionary:", end=f'\n{cars}\n\n')

try:
    delete_item('Mercedes')
    print("Remove Mercedes from dictionary:", end=f'\n{cars}\n\n')
except KeyError:
    print("\tError: There is no such key in the dictionary\n")

cars.popitem()
print("Remove last item from dictionary:", end=f'\n{cars}\n\n')

print("Keys: ", end='\n')
for key in cars.keys():
    print(key)

print("\nValues: ", end='\n')
for values in cars.values():
    print(values)

print("\nDictionary: ", end='\n')
for key, values in cars.items():
    print(f"car: {key}, cars: {values}")

cars.clear()
print("\nClear dictionary:", end=f'\n{cars}\n\n')