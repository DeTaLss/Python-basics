from functools import reduce


def composit(num_1, num_2):
    return num_1 * num_2


my_list = [num for num in range(100, 1001, 2)]
print(my_list)
print(reduce(composit, my_list))
