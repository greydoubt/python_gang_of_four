'''This code demonstrates the Adapter pattern, which allows objects with incompatible interfaces to work together, the Strategy pattern, which defines a family of algorithms, encapsulates each one, and makes them interchangeable, and NumPy, which is a powerful library for scientific computing with Python. In this example, `Adaptee` is the class that has an incompatible interface with `Client`, so we create an `Adapter` to make them work together. `Strategy` is the interface that defines the family of algorithms, and `ConcreteStrategy1` and `ConcreteStrategy2` are the concrete strategies that provide different implementations of the algorithms. Finally, `Client` is the object that uses the strategy to execute the algorithm on the data. We generate a 2D NumPy array with fake data in `Adaptee`, and use it to perform different operations with the strategies. 
'''

import numpy as np

class Adapter:
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def process_data(self):
        data = self.adaptee.get_data()
        return np.array(data)

class Adaptee:
    def get_data(self):
        return [[1, 2], [3, 4], [5, 6]]

class Strategy:
    def __init__(self, data):
        self.data = data

    def execute(self):
        pass

class ConcreteStrategy1(Strategy):
    def execute(self):
        return np.sum(self.data)

class ConcreteStrategy2(Strategy):
    def execute(self):
        return np.mean(self.data)

class Client:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def execute_strategy(self):
        return self.strategy.execute()

# Usage
adapter = Adapter(Adaptee())
data = adapter.process_data()

strategy1 = ConcreteStrategy1(data)
strategy2 = ConcreteStrategy2(data)

client = Client(strategy1)
print(client.execute_strategy())

client.set_strategy(strategy2)
print(client.execute_strategy())