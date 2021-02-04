class Stationery:
    def __init__(self, title="канцелярская принадлежность"):
        self.title = title

    def draw(self):
        print(f"Напишем с помощью {self.title}")


class Pen(Stationery):
    def draw(self):
        print(f"Пишем канцелярской принадлежностью {self.title} ручка")


class Pencil(Stationery):
    def draw(self):
        print(f"Пишем канцелярской принадлежностью {self.title} карандаш")


class Marker(Stationery):
    def draw(self):
        print(f"Пишем канцелярской принадлежностью {self.title} маркер")


attribute = Stationery()
attribute.draw()
pen = Pen("синяя")
pen.draw()
pencil = Pencil("красный")
pencil.draw()
marker = Marker("черный")
marker.draw()
