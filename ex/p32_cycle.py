

class Cycle():
    def __init__(self, lst) -> None:
        self.lst = lst

    def __iter__(self):
        self.index = -1
        return self

    def __next__(self):
        self.index += 1
        if len(self.lst) <= self.index:
            self.index = 0

        return self.lst[self.index]


def generate_pattern_array(max_length):
    increasing = ["-" * i for i in range(1, max_length + 1)]
    decreasing = ["-" * i for i in range(max_length - 1, 0, -1)]
    return increasing + decreasing


cycle = Cycle(generate_pattern_array(200))

for i in cycle:
    print(i)
