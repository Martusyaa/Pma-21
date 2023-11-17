from abc import abstractmethod, ABC


class Color(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def print_color(self):
        pass


class Blue(Color):

    def print_color(self):
        return self.__class__.__name__


class Red(Color):

    def print_color(self):
        return self.__class__.__name__


class Pink(Color):
    def print_color(self):
        return self.__class__.__name__