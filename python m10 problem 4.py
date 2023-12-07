import random

class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change):
        self.current_speed += change
        self.current_speed = max(0, min(self.current_speed, self.maximum_speed))

    def drive(self, hours):
        distance_traveled = self.current_speed * hours
        self.travelled_distance += distance_traveled

class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            car.accelerate(random.randint(-10, 15))
            car.drive(1)

    def print_status(self):
        print(f"\n{'Car':<15}{'Speed (km/h)':<15}{'Distance (km)':<15}")
        for car in self.cars:
            print(f"{car.registration_number:<15}{car.current_speed:<15.2f}{car.travelled_distance:<15.2f}")

    def race_finished(self):
        return any(car.travelled_distance >= self.distance for car in self.cars)

def main():
    cars_for_race = [Car(f"Car-{i}", random.randint(100, 200)) for i in range(1, 11)]

    grand_demolition_derby = Race(name="Grand Demolition Derby", distance=8000, cars=cars_for_race)

    hour_count = 0
    while not grand_demolition_derby.race_finished():
        grand_demolition_derby.hour_passes()
        hour_count += 1

        if hour_count % 10 == 0 or grand_demolition_derby.race_finished():
            print(f"\nRace Progress after {hour_count} hours:")
            grand_demolition_derby.print_status()

    print("\nRace Finished!")

if __name__ == "__main__":
    main()
