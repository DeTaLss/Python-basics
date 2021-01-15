proceeds = float(input("Введите знаниче выручки: "))
costs = float(input("Введите знаниче издержек: "))

if proceeds < costs:
    print("Фирма отработала с убытком:", proceeds - costs)
elif proceeds == costs:
    print("Фирма отработала в ноль")
else:
    profit = proceeds - costs
    profitability = profit / proceeds
    people = int(input("Введите число сотрудников фирмы: "))
    prof_on_people = profit / people
    print(f"Фирма отработала с прибылью: {profit}, рентабельность выручки составила: {profitability:.2f},",
          f"прибыль фирмы в расчете на одного сотрудника составила: {prof_on_people:.2f}")