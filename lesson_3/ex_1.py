def my_nums(num_1, num_2):
    div = int(num_1) / int(num_2)
    print(f"Частное: {div:.2f}")


try:
    my_nums(input("Введите делимое: "), input("Введите делитель: "))
except ZeroDivisionError:
    print("На ноль делить нельзя")
except ValueError:
    print("Вводить только числа")
