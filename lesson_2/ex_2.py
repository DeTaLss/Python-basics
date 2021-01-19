my_list = list(input("Введите значиния для списка без пробелов: "))

for indx in range(1, len(my_list), 2):
    my_list[indx - 1], my_list[indx] = my_list[indx], my_list[indx - 1]

print(my_list)
