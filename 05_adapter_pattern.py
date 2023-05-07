'''demonstrates the Adapter pattern, which converts the interface of a class into another interface that clients expect. In this example, Target is the interface expected by the client, and Adaptee is the class with the incompatible interface. Adapter is a class that adapts the interface of Adaptee to match Target. The request method is overridden by Adapter to call the specific_request method of Adaptee in a way that is compatible with the Target interface.'''


class Target:
    def request(self):
        pass

class Adaptee:
    def specific_request(self):
        return "Adaptee"

class Adapter(Target):
    def __init__(self, adaptee):
        self._adaptee = adaptee

    def request(self):
        return f"Adapter({self._adaptee.specific_request()})"

# Usage:
adaptee = Adaptee()
adapter = Adapter(adaptee)

print(adaptee.specific_request())
print(adapter.request())
