class Person:
    def __init__(self, name, age, location):
        self.name = name
        self.age = age
        self.location = location

    def __str__(self):
        return f"Person(name='{self.name}', age={self.age}, location='{self.location}')"

people_dict = {
    'person1': Person('John', 25, 'City1'),
    'person2': Person('Alice', 30, 'City2'),
    'person3': Person('Bob', 22, 'City3')
}


print("Список осіб:")
for person, details in people_dict.items():
    print(f"{person}: {details}")

people_dict['person1'].age = 26
print("\nЗмінений вік для person1:")
print(people_dict['person1'])

people_dict['person4'] = Person('Eve', 28, 'City4')
print("\nДодана нова особа:")
print(people_dict['person4'])

del people_dict['person2']
print("\nВидалена особа (person2):")
print(people_dict)

print("\nОновлений список осіб:")
for person, details in people_dict.items():
    print(f"{person}: {details}")
