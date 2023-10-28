from abc import ABC


class Color(ABC):

    def __init__(self, color=None):
        self.color = color

    def getColor(self):
        return self.color

    def __str__(self):
        return f"{self.color}"


class Blue(Color):

    def __init__(self):
        super().__init__("Blue")


class Green(Color):

    def __init__(self):
        super().__init__("Green")


class Red(Color):

    def __init__(self):
        super().__init__("Red")
