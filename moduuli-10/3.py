class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def go_to_floor(self, floor):
        if floor < self.bottom_floor or floor > self.top_floor:
            return

        if self.current_floor < floor:
            for i in range(floor - self.current_floor):
                self.floor_up()
                print(f'Current floor: {self.current_floor}')

        elif self.current_floor > floor:
            for i in range(self.current_floor - floor):
                self.floor_down()
                print(f'Current floor: {self.current_floor}')

        else:
            print(f'Current floor: {self.current_floor}')
            return

    def floor_up(self):
        self.current_floor += 1

    def floor_down(self):
        self.current_floor -= 1


class Building:
    def __init__(self, bottom_floor, top_floor, elevator):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevator = elevator
        self.elevators = [
            Elevator(bottom_floor, top_floor)
            for i in range(elevator)
        ]

    def run_elevator(self, elevator_index, target_floor):
        if 0 <= elevator_index < len(self.elevators):
            selected_elevator = self.elevators[elevator_index]
            selected_elevator.go_to_floor(target_floor)
        else:
            print(f"Elevator {elevator_index} does not exist.")

    def fire_alarm(self):
        for i, elevator in enumerate(self.elevators):
            elevator.go_to_floor(self.bottom_floor)


#  h = Elevator(1, 10)
#  print("Basic elevator test:")
#  h.go_to_floor(5)
#  h.go_to_floor(1)

# Test Building with multiple elevators

#  building = Building(1, 10, 3)
#  building.run_elevator(0, 5)
#  building.run_elevator(1, 3)
#  building.run_elevator(2, 8)

# Test single elevator building

#  small_building = Building(0, 5, 1)
#  mall_building.run_elevator(0, 4)

# Test larger building

#  office = Building(1, 6, 5)
#  office.run_elevator(0, 4)
#  office.run_elevator(4, 2)
