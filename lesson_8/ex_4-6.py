class Warehouse:
    equipment = []
    name = ""

    def __init__(self, name):
        self.equipment = []
        self.name = name

    def get_equipment_list(self):
        for i in self.equipment:
            print(f"Тип оборудования: {i.equipment_type}, Модель: {i.model}, Серийный номер: {i.serial_number}, "
                  f"Отдел: {'общий' if not i.department else i.department}")

    def give_out(self, model_name, department_name):
        for i in self.equipment:
            if i.model == model_name and i.department == "":
                i.department = department_name
                break
        else:
            print(f"Нет оборудования {model_name} в наличии")

    def return_from_department(self, model_name, department_name):
        for i in self.equipment:
            if i.model == model_name and i.department == department_name:
                i.department = ""
                break
        else:
            print(f"Нет оборудования {model_name} в наличии для возврата")

    def take_to_warehouse(self, obj):
        for i in self.equipment:
            if i.serial_number == obj.serial_number and i.equipment_type == obj.equipment_type:
                print(f"Нельзя использовать один серийный номер: {i.serial_number} "
                      f"для {i.equipment_type}")
                break
        self.equipment.append(obj)

    def free_to_use(self, model_name):
        for i in self.equipment:
            if i.model == model_name:
                return True


class OfficeEquipment:
    model = ""
    serial_number = ""
    department = ""
    equipment_type = ""


class Printer(OfficeEquipment):
    toner_model = ""
    format_size = ()

    def __init__(self, equipment_type, model, serial_number, format_size=(), toner_model=""):
        self.model = model
        self.serial_number = serial_number
        self.format_size = format_size
        self.toner_model = toner_model
        self.equipment_type = equipment_type


class Scanner(OfficeEquipment):
    scanner_size = ()

    def __init__(self, equipment_type, model, serial_number, scanner_size=()):
        self.model = model
        self.serial_number = serial_number
        self.scanner_size = scanner_size
        self.equipment_type = equipment_type


class Copier(OfficeEquipment):
    format_size = ()

    def __init__(self, equipment_type, model, serial_number, format_size=()):
        self.model = model
        self.serial_number = serial_number
        self.format_size = format_size
        self.equipment_type = equipment_type


my_warehouse = Warehouse("Офисный склад")
my_warehouse.take_to_warehouse(Printer("Принтер", "HP1550", "aWFGHw034", ('A3', 'A4'), "CN1550D"))
my_warehouse.take_to_warehouse(Printer("Принтер", "HP1451", "aQWErw545", ('A3', 'A4'), "CN1550D"))
my_warehouse.take_to_warehouse(Scanner("Сканер", "HP1856", "aWASyw986", ('A4', 'A5')))
my_warehouse.take_to_warehouse(Scanner("Сканер", "HP1220", "aWEtrWsw437", ('A4', 'A5')))
my_warehouse.take_to_warehouse(Copier("Ксерокс", "HP1243", "aWEW456sw437", ('A4', 'A5')))
my_warehouse.take_to_warehouse(Copier("Ксерокс", "HP1227", "aWEW34sw437", ('A4', 'A5')))
my_warehouse.take_to_warehouse(Copier("Ксерокс", "HP1227", "aWEW34sw437", ('A4', 'A5')))
my_warehouse.get_equipment_list()
print("Техника для IT отдела")
my_warehouse.give_out("HP1550", "IT")
my_warehouse.give_out("HP1451", "IT")
my_warehouse.give_out("HP1220", "IT")
my_warehouse.give_out("HP1550", "IT")

my_warehouse.get_equipment_list()
print("Вернуть все оборудование из IT отдела")
my_warehouse.return_from_department("HP1550", "IT")
my_warehouse.return_from_department("HP1451", "IT")
my_warehouse.return_from_department("HP1220", "IT")

my_warehouse.get_equipment_list()
