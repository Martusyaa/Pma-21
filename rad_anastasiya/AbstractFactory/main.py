from __future__ import annotations
from FactoryAbstraction import AbstractFactory
from FirstConcreteFactory import FirstConcreteFactory
from SecondConcreteFactory import SecondConcreteFactory


def client_code(factory: AbstractFactory) -> None:
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()

    print(f"{product_b.useful_function_b()}")
    print(f"{product_b.another_useful_function_b(product_a)}", end="")


if __name__ == "__main__":
    print("Client: Testing client code with the first abstract-factory type:")
    client_code(FirstConcreteFactory())

    print("\n")

    print("Client: Testing the same client code with the second abstract-factory type:")
    client_code(SecondConcreteFactory())
