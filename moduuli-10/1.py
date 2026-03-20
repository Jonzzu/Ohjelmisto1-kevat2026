class Elevator:
    def __init__(self, min_floor, max_floor):
        self.min_floor = min_floor
        self.max_floor = max_floor
        self.current_floor = min_floor

    def go_to_floor(self, floor):
        if floor < self.min_floor or floor > self.max_floor:
            return

        if self.current_floor < floor:
            for i in range(floor -self.current_floor):
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

# h = Elevator(1, 10)
# print("Basic elevator test:")
# h.go_to_floor(5)
# h.go_to_floor(1)
