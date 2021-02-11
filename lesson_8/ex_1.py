class Data:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def ent_date(cls, date):
        day = str(date.split("-")[0])
        month = str(date.split("-")[1])
        year = str(date.split("-")[2])
        Data.check_date(cls(day, month, year))
        return cls(day, month, year)

    @staticmethod
    def check_date(obj):
        if int(obj.year) <= 0:
            print(f"В году есть ошибки {obj.year}")
        else:
            print(f"Год {obj.year}")
        if int(obj.month) > 12 or int(obj.month) <= 0:
            print(f"В месяце есть ошибки {obj.month}")
        else:
            print(f"Месяц {obj.month}")
        if int(obj.month) in [1, 3, 5, 7, 8, 10, 12] and (31 >= int(obj.day) > 0):
            print(f"День {obj.day} в месяце {obj.month}")
        elif int(obj.month) in [4, 6, 9, 11] and (30 >= int(obj.day) > 0):
            print(f"День {obj.day} в месяце {obj.month}")
        elif int(obj.month) == 2 and ((29 if int(obj.year) % 4 == 0 else 28) >= int(obj.day) > 0):
            print(f"День {obj.day} в месяце {obj.month}")
        else:
            print(f"Нет такого дня {obj.day} в месяце {obj.month} в {obj.year} году")


my_date = "04-06-2010"
try:
    a = Data.ent_date(my_date)
except ValueError as error:
    print(f"Неправильные символы: {error}")
