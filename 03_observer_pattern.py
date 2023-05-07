'''demonstrates the Observer pattern, which defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically. In this example, Subject is the superclass of ConcreteSubject, which represents the object being observed. Observer is the superclass of ConcreteObserverA and ConcreteObserverB, which represent the objects observing the subject. The attach, detach, and notify methods are used to manage the observers and notify them of changes in the subject's state'''

class Observer:
    def update(self, subject):
        pass

class Subject:
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update(self)

class ConcreteSubject(Subject):
    def __init__(self):
        super().__init__()
        self.state = None

    def get_state(self):
        return self.state

    def set_state(self, state):
        self.state = state
        self.notify()

class ConcreteObserverA(Observer):
    def update(self, subject):
        print("Observer A received update:", subject.get_state())

class ConcreteObserverB(Observer):
    def update(self, subject):
        print("Observer B received update:", subject.get_state())

# Usage:
subject = ConcreteSubject()
observer_a = ConcreteObserverA()
observer_b = ConcreteObserverB()

subject.attach(observer_a)
subject.attach(observer_b)

subject.set_state("new state")
