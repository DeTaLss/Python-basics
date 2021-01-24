def my_func(x, y):
    elev = x ** y
    print(f"Возведенное число в степень получится: {elev:.4f}")


try:
    my_func(float(input("Введите действительное положительное число: ")),
            int(input("Введите целое отрицательное число: ")))
except ValueError:
    print("Вводить только числа")
