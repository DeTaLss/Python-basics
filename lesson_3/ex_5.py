def my_nums():
    num = 0
    while True:
        list = input("Введите числа через пробел или введите 'w' для завершения: ").split()
        for chis in list:
            if chis == "w":
                return num
            else:
                try:
                    num += int(chis)
                except ValueError:
                    print("Для завершения введите 'w'")
        print("Сумма чисел =", num)


print("Сумма чисел =", my_nums())
