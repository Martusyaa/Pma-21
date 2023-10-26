from abc import ABC, abstractmethod


class Color(ABC):

    @abstractmethod
    def draw(self):
        pass
