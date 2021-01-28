from random import randint

random_nums = [randint(1, 15) for _ in range(15)]
unique_nums = [num for num in random_nums if random_nums.count(num) == 1]
print(random_nums)
print(unique_nums)
