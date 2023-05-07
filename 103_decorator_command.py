'''This code demonstrates the Decorator pattern, which adds new behaviors to an object dynamically by wrapping it with another object, the Command pattern, which encapsulates a request as an object, allowing you to parameterize clients with different requests, queue or log requests, and support undoable operations, and NumPy, which is a powerful library for scientific computing with Python. In this example, Component is the interface that defines the component to be decorated, ConcreteComponent is the concrete component that provides the base implementation, Decorator is the abstract decorator that wraps the component, and ConcreteDecorator1 and ConcreteDecorator2 are the concrete decorators that provide different behaviors to the component. Invoker is the object that stores the commands and executes them, and Command is the interface that defines the command. ConcreteCommand1 and ConcreteCommand2 are the concrete commands that execute the base component and the decorated component, respectively. We generate a 2D NumPy array with fake data in ConcreteComponent, and apply different decorators to it, such as transposing and flipping the matrix, using ConcreteDecorator1 and ConcreteDecorator2, respectively. We also create two commands, ConcreteCommand1 and ConcreteCommand2, that execute the base component and the decorated component, respectively, and add them to the Invoker. Finally, we execute the commands to perform the data transformations.'''



import numpy as np

class Component:
    def execute(self):
        pass

class ConcreteComponent(Component):
    def execute(self):
        return np.array([[1, 2], [3, 4]])

class Decorator(Component):
    def __init__(self, component):
        self.component = component

    def execute(self):
        pass

class ConcreteDecorator1(Decorator):
    def execute(self):
        data = self.component.execute()
        return np.transpose(data)

class ConcreteDecorator2(Decorator):
    def execute(self):
        data = self.component.execute()
        return np.flip(data, axis=0)

class Invoker:
    def __init__(self):
        self.commands = []

    def add_command(self, command):
        self.commands.append(command)

    def execute_commands(self):
        for command in self.commands:
            command.execute()

class Command:
    def execute(self):
        pass

class ConcreteCommand1(Command):
    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        self.receiver.execute()

class ConcreteCommand2(Command):
    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        self.receiver.execute()

# Usage:
component = ConcreteComponent()

decorator1 = ConcreteDecorator1(component)
decorator2 = ConcreteDecorator2(decorator1)

invoker = Invoker()
command1 = ConcreteCommand1(component)
command2 = ConcreteCommand2(decorator2)
invoker.add_command(command1)
invoker.add_command(command2)

invoker.execute_commands()
