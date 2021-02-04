class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"profit": wage, "bonus": bonus}


class Position(Worker):
    def inp_name(self):
        return f"{self.name} {self.surname}"

    def inp_income(self):
        return f"{sum(self._income.values())}"


employee = Position("Billy", "Bonts", "tester", 350000, 60000)
print(employee.inp_name())
print(employee.position)
print(employee.inp_income())
