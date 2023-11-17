from __future__ import annotations
from abc import ABC, abstractmethod

class AbstractProductB(ABC):
    @abstractmethod
    def useful_function_b(self) -> None:
        pass

    @abstractmethod
    def another_useful_function_b(self, collaborator: AbstractProductA) -> None:
        pass

class AbstractProductA(ABC):


    @abstractmethod
    def useful_function_a(self) -> str:
        pass

