from abc import ABC, abstractmethod

class TransportFactory(ABC):
    @abstractmethod
    def create_car(self):
        pass

    @abstractmethod
    def create_motorcycle(self):
        pass

class RedTransportFactory(TransportFactory):
    def create_car(self):
        return RedCar()

    def create_motorcycle(self):
        return RedMotorcycle()

class BlueTransportFactory(TransportFactory):
    def create_car(self):
        return BlueCar()

    def create_motorcycle(self):
        return BlueMotorcycle()

class Car(ABC):
    @abstractmethod
    def demonstration(self):
        pass

class Motorcycle(ABC):
    @abstractmethod
    def demonstration(self):
        pass

class RedCar(Car):
    def demonstration(self):
        return "Red Car"

class BlueCar(Car):
    def demonstration(self):
        return "Blue Car"

class RedMotorcycle(Motorcycle):
    def demonstration(self):
        return "Red Motorcycle"

class BlueMotorcycle(Motorcycle):
    def demonstration(self):
        return "Blue Motorcycle"

# Клієнтський код
def create_transport(factory):
    car = factory.create_car()
    motorcycle = factory.create_motorcycle()

    print(car.demonstration())
    print(motorcycle.demonstration())