# Робота із словниками. Створити словник з певною структурою( пропозиція вигадати структуру самому). 
# А також навчитись виводити , видалаяти, змінювати елементи. Продемонструвати роботу програми.

class Color:
    def __init__(self, color:str):
        self.color = color
        
    def __str__(self) -> str:
        return self.color
    
def main():
    dictionary = {
        "blue":[f"{Color('Blue')}", f"{Color('Light blue')}", f"{Color('Purple')}"],
        "red":f"{Color('Red')}"
        }
    dictionary["green"] = f'{Color("Green")}'
    print(dictionary.items())
    print("-"*30)
    dictionary.pop("green")
    print(dictionary.items())
    print("-"*30)
    dictionary["red"] = str(Color("New red"))
    print(dictionary.items())
    print("-"*30)
    dictionary["blue"][1] = str(Color("New light blue"))
    print(dictionary.items())
    print("-"*30)
    print(dictionary.get("blue"))
    print("-"*30)
    print(dictionary.keys())
    print("-"*30)
    for k in dictionary.keys():
        print(dictionary.get(k))
    print("-"*30)
    for v in dictionary.values():
        print(v)
    print("-"*30)
    dictionary.clear()
    print(dictionary)
    
main()