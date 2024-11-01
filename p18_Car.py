class Car:

    def __init__(self, gas_consumption: float, tank_size: float = 30) -> None:
        self.gas_consumption = gas_consumption
        self.tank_size = tank_size
        self.tank_level = 0

    def fill_up(self, liters = None):
        if liters is None:
            self.tank_level = self.tank_size
        else:
            self.tank_level += liters

    def drive(self, distance_km: float):
        self.tank_level -= self.gas_consumption * distance_km / 100



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