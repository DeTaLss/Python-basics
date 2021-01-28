from sys import argv


def pay():
    try:
        time, rate, prem = map(float, argv[1:])
        print(f"расчетная зарплата: {time * rate + prem}")
    except ValueError:
        print("Нужну задать 3 числа")


pay()
