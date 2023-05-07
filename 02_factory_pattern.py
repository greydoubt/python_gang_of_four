'''demonstrates the Factory pattern, which provides an interface for creating objects in a superclass, while allowing subclasses to alter the type of objects that will be created. In this example, Product is the superclass of ConcreteProductA and ConcreteProductB, which represent different types of products. Creator is the superclass of ConcreteCreatorA and ConcreteCreatorB, which create instances of the products. The factory_method method is overridden by the subclasses to specify which product to create.'''

class Product:
    def operation(self):
        pass

class ConcreteProductA(Product):
    def operation(self):
        print("Operation A")

class ConcreteProductB(Product):
    def operation(self):
        print("Operation B")

class Creator:
    def factory_method(self):
        pass

    def do_something(self):
        product = self.factory_method()
        product.operation()

class ConcreteCreatorA(Creator):
    def factory_method(self):
        return ConcreteProductA()

class ConcreteCreatorB(Creator):
    def factory_method(self):
        return ConcreteProductB()

# Usage:
creator_a = ConcreteCreatorA()
creator_a.do_something()

creator_b = ConcreteCreatorB()
creator_b.do_something()
