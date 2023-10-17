from abc import ABC, abstractmethod

class Color(ABC):
    def __init__(self):
        self.color:str

class Red(Color):
    def __init__(self):
        super().__init__()
        self.color = "RED <З"

    def __str__(self):
        return self.color

class Black(Color):
    def __init__(self):
        super().__init__()
        self.color = "Black."

    def __str__(self):
        return self.color

class Gold(Color):
    def __init__(self):
        super().__init__()
        self.color = "Gold"

    def __str__(self):
        return self.color