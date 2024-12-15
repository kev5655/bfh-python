
class MyRange:
    def __init__(self, range):
        self.range = range

    def __iter__(self):
        self.current = 0
        return self

    def __next__(self):
        x = self.current
        if x <= self.range:
            self.current += 1
            return x
        else:
            raise StopIteration()


ra = MyRange(10)

for i in ra:
    print(i)
