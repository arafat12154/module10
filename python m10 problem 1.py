class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.current_floor = bottom_floor
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor

    def go_to_floor(self, target_floor):
        if target_floor > self.current_floor:
            self.floor_up(target_floor)
        elif target_floor < self.current_floor:
            self.floor_down(target_floor)

    def floor_up(self, target_floor):
        while self.current_floor < target_floor:
            self.current_floor += 1
            print(f"Elevator is at floor {self.current_floor}")

    def floor_down(self, target_floor):
        while self.current_floor > target_floor:
            self.current_floor -= 1
            print(f"Elevator is at floor {self.current_floor}")

def main():
    my_elevator = Elevator(bottom_floor=1, top_floor=10)
    my_elevator.go_to_floor(5)

    my_elevator.go_to_floor(1)
if __name__ == "__main__":
    main()
