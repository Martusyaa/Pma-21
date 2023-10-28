class Person:
    def __init__(self, name:str, age:int):
        self.name = name
        self.age = age
    
    
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}\n"