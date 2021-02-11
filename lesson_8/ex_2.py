class MyException(Exception):
    def __init__(self, message):
        self.message = message


try:
    num_1 = int(input("Введите делимое: "))
    num_2 = int(input("Введите делитель: "))
    if num_2 == 0:
        raise MyException("На 0 делить нельзя")
except (ValueError, MyException) as error:
    print(error)
else:
    print(num_1 / num_2)
