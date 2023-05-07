'''demonstrates the Decorator pattern, which attaches additional responsibilities to an object dynamically. In this example, Component is the superclass of ConcreteComponent, which represents the basic object being decorated. Decorator is the superclass of ConcreteDecoratorA and ConcreteDecoratorB, which add additional functionality to the object. The operation method is overridden by the decorators to add their own functionality before or after calling the base component's operation method.'''


class Component:
    def operation(self):
        pass

class ConcreteComponent(Component):
    def operation(self):
        return "ConcreteComponent"

class Decorator(Component):
    def __init__(self, component):
        self._component = component

    def operation(self):
        return self._component.operation()

class ConcreteDecoratorA(Decorator):
    def operation(self):
        return f"ConcreteDecoratorA({self._component.operation()})"

class ConcreteDecoratorB(Decorator):
    def operation(self):
        return f"ConcreteDecoratorB({self._component.operation()})"

# Usage:
component = ConcreteComponent()
decorator_a = ConcreteDecoratorA(component)
decorator_b = ConcreteDecoratorB(decorator_a)

print(component.operation())
print(decorator_a.operation())
print(decorator_b.operation())
