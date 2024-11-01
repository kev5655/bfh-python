class Car:
    """
    Represents a car that has a certain gas consumption (measured in liters/100km),
    and the car's tank has a certain gas level (measured in liters). Most cars have a tank size of 30 l.
    """

    def __init__(self, consumption: float, tank_size: float = 30.0) -> None:
        """
        Constructor using keyword argument for the tankSize with default value
        :param consumption: car's consumption in liters/100km
        :param tank-size: (keyword argument) in liters
        """
        self.consumption = consumption
        self.tank_size = tank_size
        self.tank_level = 0.0

    def fill_up(self, liters: float = 0.0) -> None:
        """
        Fill up the tank with a given amount of gas, if no parameter is provided
        then the tank will be completely filled-up.
        :return: None
        """
        if liters is None:
            # The tank is completely filled-up
            self.tank_level = self.tank_size
        else:
            # The tank will not overflow
            self.tank_level = min(self.tank_size, self.tank_level + liters)

    def drive(self, distance: float) -> None:
        """
        Simulates that the car travels a certain distance
        :param distance: the distance to travel
        """
        self.tank_level -= max(distance * self.consumption / 100, 0.0)


def main() -> None:
    """ Launcher """
    car1 = Car(5.0, 50.0)
    print("Tank level car 1: " + str(car1.tank_level))
    car1.fill_up()
    print("Tank level car 1 (after fill-up): " + str(car1.tank_level))
    car1.drive(100.0)
    print("Tank level car 1 (after 100km): " + str(car1.tank_level))  # 45.0

    car2 = Car(3.0)
    print("Tank level car 2: " + str(car2.tank_level))
    car2.fill_up(20.0)
    print("Tank level car 2 (after fill-up): " + str(car2.tank_level))
    car2.drive(150.0)
    print("Tank level car 2 (after 150km): " + str(car2.tank_level))  # 15.5


if __name__ == "__main__":
    main()
