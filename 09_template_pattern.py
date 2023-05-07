'''demonstrates the Template Method pattern, which defines the skeleton of an algorithm in a superclass but lets subclasses override specific steps of the algorithm without changing its structure. In this example, AbstractClass is the superclass that defines the template method, which calls two primitive operations that are overridden by ConcreteClass1 and ConcreteClass2, which are the subclasses that implement the algorithm.'''

class AbstractClass:
    def template_method(self):
        self._primitive_operation1()
        self._primitive_operation2()

    def _primitive_operation1(self):
        pass

    def _primitive_operation2(self):
        pass

class ConcreteClass1(AbstractClass):
    def _primitive_operation1(self):
        return "ConcreteClass1: primitive operation 1"

    def _primitive_operation2(self):
        return "ConcreteClass1: primitive operation 2"

class ConcreteClass2(AbstractClass):
    def _primitive_operation1(self):
        return "ConcreteClass2: primitive operation 1"

    def _primitive_operation2(self):
        return "ConcreteClass2: primitive operation 2"

# Usage:
abstract_class = ConcreteClass1()
result = abstract_class.template_method()
print(result)

abstract_class = ConcreteClass2()
result = abstract_class.template_method()
print(result)
