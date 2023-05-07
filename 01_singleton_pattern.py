''' simple implementation of the Singleton pattern, which ensures that only one instance of a class is created throughout the lifetime of an application. The _instance class variable keeps track of the single instance, and the __new__ method is overridden to ensure that the instance is only created if it doesn't already exist.'''


class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

# Usage:
s1 = Singleton()
s2 = Singleton()

print(s1 is s2)  # True
