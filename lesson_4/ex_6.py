from itertools import count, cycle

start_num = count(5)
start_list = cycle("abcdefghijkl")

for i in range(10):
    print("число и элемент списка:", next(start_num), "-", next(start_list))
