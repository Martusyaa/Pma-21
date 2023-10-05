from FactoryAbstraction import AbstractFactory
from ProductAbstraction import AbstractProductA, AbstractProductB
from SecondConcreteProductA import SecondConcreteProductA
from SecondConcreteProductB import SecondConcreteProductB


class SecondConcreteFactory(AbstractFactory):

    def create_product_a(self) -> AbstractProductA:
        return SecondConcreteProductA()

    def create_product_b(self) -> AbstractProductB:
        return SecondConcreteProductB()