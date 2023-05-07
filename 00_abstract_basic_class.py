from abc import ABC, abstractmethod

class MyIterator(ABC):
    @abstractmethod
    def __iter__(self):
        pass

    @abstractmethod
    def __next__(self):
        pass

class MyGenerator(MyIterator):
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.n:
            result = self.current
            self.current += 1
            return result
        else:
            raise StopIteration

class MyDataStructure:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        return iter(self.data)

my_gen = MyGenerator(5)
for i in my_gen:
    print(i)

my_data = MyDataStructure([1, 2, 3, 4, 5])
for i in my_data:
    print(i)

# Using these classes with NumPy
import numpy as np

class MyNumpyIterator(ABC):
    @abstractmethod
    def __iter__(self):
        pass

class MyNumpyArray(MyNumpyIterator):
    def __init__(self, data):
        self.data = np.array(data)

    def __iter__(self):
        return np.nditer(self.data)

my_np_array = MyNumpyArray([1, 2, 3, 4, 5])
for i in my_np_array:
    print(i)

# Using these classes with list comprehensions
my_list = MyDataStructure([1, 2, 3, 4, 5])
my_gen = MyGenerator(5)

# Using list comprehension with MyDataStructure
my_list_squared = [x**2 for x in my_list]
print(my_list_squared)

# Using list comprehension with MyGenerator
my_gen_squared = [x**2 for x in my_gen]
print(my_gen_squared)
