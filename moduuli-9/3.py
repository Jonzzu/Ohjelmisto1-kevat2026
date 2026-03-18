class Car:
    def __init__(self, license_plate, maximum_speed, current_speed=0, travelled_distance=0):
        self.license_plate = license_plate
        self.maximum_speed = maximum_speed
        self.current_speed = current_speed
        self.travelled_distance = travelled_distance

    def accelerate(self, speed_delta=0):
        new_speed = self.current_speed + speed_delta

        if self.maximum_speed >= new_speed >= 0:
            self.current_speed = new_speed
        else:
            self.current_speed = 0
        return

    def drive(self,time_hours=0):
        distance_travelled = self.current_speed * time_hours

        self.travelled_distance = self.travelled_distance + distance_travelled
        return
