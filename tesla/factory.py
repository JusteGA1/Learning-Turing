class Tesla:
    def __init__(self, model: str, color: str, autopilot: bool = False):
        self.__model = model
        self.__battery_charge = 99.9
        self.__is_locked = True
        self.__seats_count = 5
        self.__color = color
        self.__autopilot = autopilot
        self.__efficiency = 0.3

    @property
    def color(self):
        return self.__color

    def welcome(self) -> str:
        raise NotImplementedError

    def autopilot(self, obsticle: str) -> str:
        if self.__autopilot:
            return f"Tesla model {self.__model} avoids {obsticle}"
        return f"Autopilot is not available"

    @property
    def seats_count(self) -> int:
        return self.__seats_count

    @seats_count.setter
    def seats_count(self, new_seat_number: int) -> int:
        """
        Returns number of seats in the car.

            Parameters:
                new_seat_number (int): integer

            Limitations:
                if entered seat number less than 2, return defaults to 5

            Returns:
                desired or default number of seats
        """
        if new_seat_number < 2:
            new_seat_number = 5
        self.__seats_count = new_seat_number

    def open_doors(self):
        if self.__is_locked:
            return "Car is locked!"
        if not self.__is_locked:
            return "Doors opens sideways"

    @property
    def is_locked(self):
        return self.__is_locked

    def unlock(self):
        self.__is_locked = False

    def lock(self):
        """
        Makes sure that the car is locked.
        """
        self.__is_locked = True

    def check_battery_level(self) -> str:
        return f"Battery charge level is {self.__battery_charge}%"

    def charge_battery(self):
        """
        Charges car battery to 100%.

        Returns battery level.
        """
        self.__battery_charge = 100
        return self.check_battery_level()

    def drive(self, travel_range: float):
        battery_discharge_percent = travel_range * self.__efficiency
        if self.__battery_charge - battery_discharge_percent >= 0:
            self.__battery_charge = self.__battery_charge - battery_discharge_percent
            return self.check_battery_level()
        return self.check_battery_level()

