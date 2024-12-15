

def generator_fibonacci():
    x1 = 0
    x2 = 1
    while True:
        x3 = x1 + x2
        yield x3
        x1 = x2
        x2 = x3


gen = generator_fibonacci()
for _ in range(15):
    print(next(gen))
