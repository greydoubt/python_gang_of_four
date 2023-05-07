'''demonstrates the State pattern, which allows an object to alter its behavior when its internal state changes. In this example, State is the superclass of ConcreteStateA and ConcreteStateB, which are the concrete states that provide different implementations of the handle method. Context is the object whose behavior changes based on its internal state, which can be set using the set_state method'''

class State:
    def handle(self):
        pass

class ConcreteStateA(State):
    def handle(self):
        return "ConcreteStateA"

class ConcreteStateB(State):
    def handle(self):
        return "ConcreteStateB"

class Context:
    def __init__(self):
        self._state = ConcreteStateA()

    def set_state(self, state):
        self._state = state

    def request(self):
        return self._state.handle()

# Usage:
context = Context()
result = context.request()
print(result)

context.set_state(ConcreteStateB())
result = context.request()
print(result)
