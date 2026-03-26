class Car:
    def __init__(self, license_plate, maximum_speed, current_speed=0, travelled_distance=0):
        self.license_plate = license_plate
        self.maximum_speed = maximum_speed
        self.current_speed = current_speed
        self.travelled_distance = travelled_distance

    def accelerate(self, speed_delta=0):
        new_speed = self.current_speed + speed_delta
        self.current_speed = max(0, min(new_speed, self.maximum_speed))

    def drive(self, time_hours=0):
        distance_travelled = self.current_speed * time_hours
        self.travelled_distance = self.travelled_distance + distance_travelled


class ElectricCar(Car):
    def __init__(self, license_plate, maximum_speed, battery_capacity):
        super().__init__(license_plate, maximum_speed)
        self.battery_capacity = battery_capacity


class GasolineCar(Car):
    def __init__(self, license_plate, maximum_speed, tank_volume):
        super().__init__(license_plate, maximum_speed)
        self.tank_volume = tank_volume
