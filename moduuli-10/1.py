class Elevator:
    def __init__(self, lowest_floor, highest_floor):
        self.lowest_floor = lowest_floor
        self.highest_floor = highest_floor
        self.current_floor = lowest_floor

    def go_to_floor(self, floor):
        if floor < self.lowest_floor or floor > self.highest_floor:
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
