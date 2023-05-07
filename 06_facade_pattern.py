'''demonstrates the Facade pattern, which provides a simplified interface to a complex system of classes. In this example, SubsystemA, SubsystemB, and SubsystemC represent a complex system of classes that can be difficult to use directly. Facade provides a simplified interface to this system, by combining the functionality of the subsystems into a single operation method that can be called with a single method call'''


class SubsystemA:
    def operation_a(self):
        return "SubsystemA"

class SubsystemB:
    def operation_b(self):
        return "SubsystemB"

class SubsystemC:
    def operation_c(self):
        return "SubsystemC"

class Facade:
    def __init__(self):
        self._subsystem_a = SubsystemA()
        self._subsystem_b = SubsystemB()
        self._subsystem_c = SubsystemC()

    def operation(self):
        result = []
        result.append(self._subsystem_a.operation_a())
        result.append(self._subsystem_b.operation_b())
        result.append(self._subsystem_c.operation_c())
        return " ".join(result)

# Usage:
facade = Facade()
print(facade.operation())
