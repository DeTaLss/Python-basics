def my_func(num_1, num_2, num_3):
    list = [num_1, num_2, num_3]
    list.remove(min(list))
    return sum(list)


try:
    print(my_func(int(input("Введите число: ")), int(input("Введите второе число: ")),
                  int(input("Введите третье число: "))))
except ValueError:
    print("Вводить только целые числа")
