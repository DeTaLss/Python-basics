class MyException(Exception):
    def __init__(self, numbers):
        self.numbers = numbers


my_list = []
while True:
    num = input("Введите число: ")
    try:
        if not num.replace("-", "").replace(",", "").replace(".", "").isdigit():
            raise MyException("Вводить только цифры")
    except (ValueError, MyException) as error:
        print(error)
        if num == "стоп":
            break
    else:
        my_list.append(num)
        print(my_list)
print(10 * "-")
print(f"Завершение, список содержит: {my_list}")
