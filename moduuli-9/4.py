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
        return

    def drive(self, time_hours=0):
        distance_travelled = self.current_speed * time_hours

        self.travelled_distance = self.travelled_distance + distance_travelled
        return


def race(cars):
    while max(car.travelled_distance for car in cars) <= 10000:
        for car in cars:
            car.accelerate(random.randint(-10, 15))
            car.drive(1)
    cars.sort(key=lambda car: car.travelled_distance, reverse=True)
    return cars


cars = []

for i in range(1, 11):
    plate = f"ABC-{i}"
    max_speed = random.randint(100, 200)
    new_car = Car(plate, max_speed)
    cars.append(new_car)

sorted_cars = race(cars)

print(f"{'Rank':<5} {'Plate':<10} {'Distance':<10}")
print("-" * 25)

for index, car in enumerate(sorted_cars):
    print(f"{index + 1:<5} {car.license_plate:<10} {car.travelled_distance:<10.2f} km")
