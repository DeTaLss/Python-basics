numbers = [200, 45, 14, 63, 8, 95, 52, 2, 18, 87]
new_nums = [numbers[num] for num in range(1, len(numbers)) if numbers[num] > numbers[num - 1]]
print(new_nums)
