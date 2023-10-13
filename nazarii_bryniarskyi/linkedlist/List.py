from abc import ABC, abstractmethod

class List(ABC):

    @abstractmethod
    def add(self, *args):
        pass

    @abstractmethod
    def get(self, index):
        pass

    @abstractmethod
    def remove(self, index):
        pass

    @abstractmethod
    def clear(self):
        pass

    @abstractmethod
    def size(self):
        pass

