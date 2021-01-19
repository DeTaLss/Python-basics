enter = input("Введите несколько слов через пробел: ")

for num, word in enumerate(enter.split(), 1):
    print(num, f"{word:.10s}")
