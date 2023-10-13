from FactoryAbstraction import AbstractFactory
from FirstConcreteProductA import FirstConcreteProductA
from FirstConcreteProductB import FirstConcreteProductB
from ProductAbstraction import AbstractProductA, AbstractProductB


class FirstConcreteFactory(AbstractFactory):

    def create_product_a(self) -> AbstractProductA:
        return FirstConcreteProductA()

    def create_product_b(self) -> AbstractProductB:
        return FirstConcreteProductB()
