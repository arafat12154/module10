import random

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

class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = [Elevator(bottom_floor, top_floor) for _ in range(num_elevators)]

    def run_elevator(self, elevator_number, destination_floor):
        if 0 <= elevator_number < len(self.elevators):
            elevator = self.elevators[elevator_number]
            elevator.go_to_floor(destination_floor)
        else:
            print("Invalid elevator number.")

def main():
    my_building = Building(bottom_floor=1, top_floor=10, num_elevators=5)
    for i in range(5):
        elevator_number = random.randint(0, 4)
        destination_floor = random.randint(1, 10)
        my_building.run_elevator(elevator_number, destination_floor)

if __name__ == "__main__":
    main()
