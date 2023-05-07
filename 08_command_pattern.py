'''uses  the following components:

    Receiver is the interface for objects that can perform an action.
    ConcreteReceiver is a concrete implementation of the Receiver interface. It defines the actual action to be performed.
    Command is the interface for commands that encapsulate actions.
    ConcreteCommand is a concrete implementation of the Command interface. It holds a reference to a Receiver object and delegates the execution of the action to that receiver.
    Invoker is the object that invokes a command. It holds a reference to a command and can execute that command.

In the usage section, we create a ConcreteReceiver object and a ConcreteCommand object, passing the receiver as a parameter to the command. We also create an Invoker object.

Next, we set the command on the invoker using the set_command method, passing the command as an argument.

Finally, we call the execute_command method on the invoker, which in turn calls the execute method on the command. The command executes the action on the receiver, and the result is returned.

In this example, the result will be the string "ConcreteReceiver", which is the result of executing the action on the ConcreteReceiver object.

This code demonstrates how the Command pattern works by encapsulating requests as objects, decoupling the sender and receiver, and allowing for flexible execution and parameterization of actions.'''


class Receiver:
    def action(self):
        pass

class ConcreteReceiver(Receiver):
    def action(self):
        return "ConcreteReceiver"

class Command:
    def execute(self):
        pass

class ConcreteCommand(Command):
    def __init__(self, receiver):
        self._receiver = receiver

    def execute(self):
        return self._receiver.action()

class Invoker:
    def __init__(self):
        self._command = None

    def set_command(self, command):
        self._command = command

    def execute_command(self):
        return self._command.execute()

# Usage:
receiver = ConcreteReceiver()
command = ConcreteCommand(receiver)
invoker = Invoker()

invoker.set_command(command)
result = invoker.execute_command()
print(result) 