class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass_of_asphalt(self):
        return f"Для покрытия дороги длинной {self._length}м и шириной {self._width}м необходимо {(self._length * self._width * 25 * 5) / 1000}т асфальта"


road_1 = Road(3600, 30)
print(road_1.mass_of_asphalt())
