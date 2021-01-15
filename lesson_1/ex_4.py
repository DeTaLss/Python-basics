number = int(input("Введите целое положительное число: "))

num_max = 0
num_ost = number

while num_ost > 0:
    num_last = num_ost % 10
    if num_last > num_max:
        num_max = num_last
        if num_max == 9:
            break
    num_ost = num_ost // 10

print("Наибольшая цифра в числе:", num_max)