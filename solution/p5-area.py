import math


def area(radius):
   """Computes the area of a disc of a given radius and returns it"""
   return math.pi * radius * radius


def main():
    """ Launcher """
    print(area(10))


if __name__ == "__main__":
    main()
