from itertools import count
from math import factorial


def gener():
    for num in count(1):
        yield factorial(num)


numbers = gener()
n = 0
for i in numbers:
    if n == 10:
        break
    else:
        n += 1
        print(f"Факториал {n} = {i}")
