time = int(input("Введите время в секундах: "))

hour = time // 3600
hour_ost = time % 3600
min = hour_ost // 60
sec = hour_ost % 60

print(f"{hour:02d}:{min:02d}:{sec:02d}")