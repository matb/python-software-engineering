class EvenNumbers(object):
    "An iterable object."

    def __init__(self, maximum):
        self.maximum = maximum

    def __iter__(self):
        return EvenIterator(self)


class EvenIterator(object):
    "An iterator."

    def __init__(self, container):
        self.container = container
        self.n = 0

    def __next__(self):
        self.n += 2
        if self.n > self.container.maximum:
            raise StopIteration
        return self.n

    def __iter__(self):
        return self


class EvenIter(object):

    def __init__(self, max):
        self.max = max
        self.n = 0

    def __next__(self):
        self.n += 2
        if self.n > self.max:
            raise StopIteration
        return self.n

    def __iter__(self):
        return self


if __name__ == '__main__':
    for n in EvenIter(7):
        print(n)