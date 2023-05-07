'''demonstrates the Factory Method pattern, which provides an interface for creating objects in a superclass, but allows subclasses to alter the type of objects that will be created, and the Abstract Factory pattern, which provides an interface for creating families of related or dependent objects without specifying their concrete classes. In this example, AbstractFactory is the interface that defines the factory methods, and ConcreteFactory1 and ConcreteFactory2 are the concrete factories that create different products. AbstractProduct is the interface that defines the product to be created, and ConcreteProduct1 and ConcreteProduct2 are the concrete products that provide different implementations. Client is the object that uses the product to execute its functionality. We generate 2D NumPy arrays with fake data in the concrete products, and use the concrete factories to create the products and the clients to execute them.'''

import numpy as np

class AbstractFactory:
    def create_product(self):
        pass

class ConcreteFactory1(AbstractFactory):
    def create_product(self):
        return ConcreteProduct1()

class ConcreteFactory2(AbstractFactory):
    def create_product(self):
        return ConcreteProduct2()

class AbstractProduct:
    def execute(self):
        pass

class ConcreteProduct1(AbstractProduct):
    def execute(self):
        return np.array([[1, 2], [3, 4]])

class ConcreteProduct2(AbstractProduct):
    def execute(self):
        return np.array([[5, 6], [7, 8]])

class Client:
    def __init__(self, factory):
        self.product = factory.create_product()

    def execute_product(self):
        return self.product.execute()

# Usage:
factory1 = ConcreteFactory1()
client1 = Client(factory1)
print(client1.execute_product())

factory2 = ConcreteFactory2()
client2 = Client(factory2)
print(client2.execute_product())
