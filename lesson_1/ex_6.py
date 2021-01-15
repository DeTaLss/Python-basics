while True:
    days = 1
    first_d = float(input("Введите сколько км преодолено в первый день: "))
    day_km = float(input("Введите желаемое колличество км для расчета дня: "))
    while first_d < day_km:
        first_d += first_d * 0.1
        days += 1
    print("Спортсмен достигнет результата на", days, "день")
    break