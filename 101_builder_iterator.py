'''demonstrates the Builder pattern, which separates the construction of a complex object from its representation, and the Iterator pattern, which provides a way to access the elements of an aggregate object sequentially without exposing its underlying representation. In this example, Product is the complex object that is being constructed, Builder is the interface that defines how the parts of the object are added, ConcreteBuilder1 and ConcreteBuilder2 are the concrete builders that provide different implementations of the parts, and Director is the object that controls the construction process. The Iterator is used to access the parts of the constructed object sequentially.'''

import numpy as np

class Product:
    def __init__(self):
        self.parts = []

    def add_part(self, part):
        self.parts.append(part)

    def list_parts(self):
        return "\n".join(self.parts)

class Builder:
    def create_product(self):
        self.product = Product()

    def add_part_a(self):
        pass

    def add_part_b(self):
        pass

    def get_product(self):
        return self.product

class ConcreteBuilder1(Builder):
    def add_part_a(self):
        self.product.add_part("Part A1")

    def add_part_b(self):
        self.product.add_part("Part B1")

class ConcreteBuilder2(Builder):
    def add_part_a(self):
        self.product.add_part("Part A2")

    def add_part_b(self):
        self.product.add_part("Part B2")

class Director:
    def set_builder(self, builder):
        self.builder = builder

    def construct(self):
        self.builder.create_product()
        self.builder.add_part_a()
        self.builder.add_part_b()

class Iterator:
    def __init__(self, collection):
        self._collection = collection
        self._position = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._position < len(self._collection):
            item = self._collection[self._position]
            self._position += 1
            return item
        else:
            raise StopIteration

# Usage:
director = Director()

builder1 = ConcreteBuilder1()
director.set_builder(builder1)
director.construct()

product = builder1.get_product()
iterator = Iterator(product.parts)
for part in iterator:
    print(part)

builder2 = ConcreteBuilder2()
director.set_builder(builder2)
director.construct()

product = builder2.get_product()
iterator = Iterator(product.parts)
for part in iterator:
    print(part)
