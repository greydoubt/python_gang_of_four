'''demonstrates the Iterator pattern, which provides a way to access the elements of an aggregate object sequentially without exposing its underlying representation. In this example, Iterator is the iterator that provides the next element of the collection each time it is called. Collection is the aggregate object that holds a collection of items and provides an iterator for it.'''


class Iterator:
    def __init__(self, collection):
        self._collection = collection
        self._position = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._position < len(self._collection):
            item = self._collection[self._position]
            self._position += 1
            return item
        else:
            raise StopIteration

class Collection:
    def __init__(self):
        self._data = []

    def add_item(self, item):
        self._data.append(item)

    def create_iterator(self):
        return Iterator(self._data)

# Usage:
collection = Collection()
collection.add_item("item 1")
collection.add_item("item 2")
collection.add_item("item 3")

iterator = collection.create_iterator()
for item in iterator:
    print(item)
