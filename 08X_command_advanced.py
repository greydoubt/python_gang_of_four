''' the Command pattern is used to encapsulate requests as objects, allowing you to parameterize clients with different requests, queue or log requests, and support undoable operations.

The Calculator class acts as the receiver, providing the actual implementation of mathematical operations like addition, subtraction, multiplication, and division. Each operation modifies the _result attribute of the calculator.

The Command class defines the interface for executing commands. Concrete command classes (AddCommand, SubtractCommand, MultiplyCommand, and DivideCommand) implement the execute method to call the respective operation on the calculator.

The Invoker class maintains a list of commands and executes them when requested. It iterates over the commands and invokes their execute method.

In the usage section, we create an instance of the calculator and invoker. We also create instances of concrete commands, passing the calculator and necessary parameters. These commands are then added to the invoker's command list. Finally, we call the execute_commands method on the invoker, which in turn executes each command in the list.

After executing the commands, we retrieve the result from the calculator and print it.

This example demonstrates how the Command pattern can be used to encapsulate and parameterize operations, providing a flexible and extensible way to handle requests in an application.
'''

import numpy as np

# Receiver
class Calculator:
    def __init__(self):
        self._result = 0

    def add(self, x, y):
        self._result = x + y

    def subtract(self, x, y):
        self._result = x - y

    def multiply(self, x, y):
        self._result = x * y

    def divide(self, x, y):
        if y != 0:
            self._result = x / y
        else:
            print("Error: Division by zero!")

    def get_result(self):
        return self._result

# Command
class Command:
    def execute(self):
        pass

# Concrete Commands
class AddCommand(Command):
    def __init__(self, calculator, x, y):
        self._calculator = calculator
        self._x = x
        self._y = y

    def execute(self):
        self._calculator.add(self._x, self._y)

class SubtractCommand(Command):
    def __init__(self, calculator, x, y):
        self._calculator = calculator
        self._x = x
        self._y = y

    def execute(self):
        self._calculator.subtract(self._x, self._y)

class MultiplyCommand(Command):
    def __init__(self, calculator, x, y):
        self._calculator = calculator
        self._x = x
        self._y = y

    def execute(self):
        self._calculator.multiply(self._x, self._y)

class DivideCommand(Command):
    def __init__(self, calculator, x, y):
        self._calculator = calculator
        self._x = x
        self._y = y

    def execute(self):
        self._calculator.divide(self._x, self._y)

# Invoker
class Invoker:
    def __init__(self):
        self._commands = []

    def add_command(self, command):
        self._commands.append(command)

    def execute_commands(self):
        for command in self._commands:
            command.execute()

# Usage
calculator = Calculator()
invoker = Invoker()

add_command = AddCommand(calculator, 5, 3)
subtract_command = SubtractCommand(calculator, 10, 4)
multiply_command = MultiplyCommand(calculator, 2, 6)
divide_command = DivideCommand(calculator, 10, 2)

invoker.add_command(add_command)
invoker.add_command(subtract_command)
invoker.add_command(multiply_command)
invoker.add_command(divide_command)

invoker.execute_commands()

result = calculator.get_result()
print("Result:", result)  # Result: 6.0
