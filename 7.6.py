import random

class BinaryIterator:
    def __init__(self):
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        value = self.current
        self.current = 1 - self.current
        return value


class RandomWalk2DIterator:
    def __init__(self):
        self.directions = ("N", "E", "S", "W")

    def __iter__(self):
        return self

    def __next__(self):
        return random.choice(self.directions)

class DaysIterator:
    def __init__(self):
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if(self.current <= 6):
            value = self.current
            self.current = 1 + self.current
        else:
            value = 0
            self.current = 1
        return value

iterator1 = BinaryIterator()
iterator2 = RandomWalk2DIterator()
iterator3 = DaysIterator()

for _ in range(10):
    print(next(iterator1))
print()
for _ in range(10):
    print(next(iterator2))
print()
for _ in range(10):
    print(next(iterator3))