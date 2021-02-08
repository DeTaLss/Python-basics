from abc import ABC, abstractmethod


class Clothes(ABC):
    result = 0

    def __init__(self, values):
        self.values = values

    @property
    @abstractmethod
    def consump(self):
        pass

    def __add__(self, other):
        Clothes.result += self.consump + other.consump
        return Costume(0)

    def __str__(self):
        return f"{Clothes.result}"


class Coat(Clothes):
    @property
    def consump(self):
        return round(self.values / 6.5) + 0.5


class Costume(Clothes):
    @property
    def consump(self):
        return round((2 * self.values + 0.3) / 100)


coat = Coat(53)
costume = Costume(191)
print(coat + costume + coat)
