class Car:
    def __init__(self, license_plate, maximum_speed, current_speed=0, travelled_distance=0):
        self.license_plate = license_plate
        self.maximum_speed = maximum_speed
        self.current_speed = current_speed
        self.travelled_distance = travelled_distance

    def accelerate(self, speed_delta=0):
        new_speed = self.current_speed + speed_delta

        if new_speed <= self.maximum_speed and new_speed >= 0:
            self.current_speed = new_speed
        else:
            self.current_speed = 0
        return


