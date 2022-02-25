from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, list):
        self.index = 0
        self.list = list

    def __next__(self):
        try:
            iteration = self.list[self.index]
        except IndexError:
            raise StopIteration()
        else:
            self.index += 1
            return iteration
