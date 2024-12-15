

def infinite(x):
    current = x
    while True:
        yield current
        current += 1


gen = infinite(10)

for _ in range(10):
    print(next(gen))
