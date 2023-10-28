from abc import abstractmethod, ABC


class Color(ABC):
    def __init__(self):
        self.color = self.__class__.__name__

    def __str__(self):
        return self.color


class Red(Color):
    pass


class Blue(Color):
    pass


class Yellow(Color):
    pass
