import random


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


class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            speed_change = random.randint(-10, 15)
            car.accelerate(speed_change)
            car.drive(1)

    def print_status(self):
        print(f"{'License plate':<15} {'Speed (km/h)':<15} {'Distance (km)':<15}")
        print("-" * 45)
        for car in self.cars:
            print(f"{car.license_plate:<15} {car.current_speed:<15.1f} {car.travelled_distance:<15.2f}")

    def race_finished(self):
        return any(car.travelled_distance >= self.distance for car in self.cars)