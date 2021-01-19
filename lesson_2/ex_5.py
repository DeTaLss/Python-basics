my_list = [9, 8, 3, 3, 2, 1]

while True:
    list_add = input("Введите елемент рейтинга(натуральное число) или "
                     "введите 'конец' если элементы больше не требуются: ")
    if list_add == "конец":
        break
    else:
        i = 0
        for num in my_list:
            if int(list_add) <= num:
                i += 1
        my_list.insert(i, int(list_add))
        print(my_list)

print(my_list)
