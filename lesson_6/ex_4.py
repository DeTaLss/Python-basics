class Car:
    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police
        print(f"Машина: {self.name}, цвет: {self.color}, машина полицеская: {self.is_police}")

    def go(self):
        print(f"{self.name} машина поехала")

    def stop(self):
        print(f"{self.name} машина остановилась")

    def turn(self, direction):
        print(f"{self.name}, машина повернула - {'налево' if direction == 0 else 'направо'}")

    def show_speed(self):
        return f"{self.name}, скорость машины - {self.speed}"


class TownCar(Car):
    def show_speed(self):
        return f"{self.name}, скорость машины - {self.speed}, скорость превышена" if self.speed > 60 else f"{self.name}, скорость машины {self.speed}"


class WorkCar(Car):
    def show_speed(self):
        return f"{self.name}, скорость машины - {self.speed}, скорость превышена" if self.speed > 40 else f"{self.name}, скорость машины {self.speed}"


class SportCar(Car):
    pass


class PoliceCar(Car):
    def __init__(self, name, color, speed, is_police=True):
        super().__init__(name, color, speed, is_police)


town_car = TownCar("Автобус", "белый", 65)
town_car.go()
town_car.turn(0)
print(town_car.show_speed())
town_car.stop()
print()

work_car = WorkCar("Камаз", "зеленый", 39)
work_car.go()
work_car.turn(1)
print(work_car.show_speed())
work_car.stop()
print()

sport_car = SportCar("Спортивная", "фиолетовая", 210)
sport_car.go()
sport_car.turn(1)
print(sport_car.show_speed())
sport_car.stop()
print()

police_car = PoliceCar("Полицейская", "синяя", 100)
police_car.go()
print(police_car.show_speed())
police_car.turn(0)
police_car.stop()
