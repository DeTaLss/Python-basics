month = int(input("Введите номер месяца: "))
month_list = ["зима", "весна", "лето", "осень"]
month_dict = {1: "зима", 2: "зима", 12: "зима", 3: "весна", 4: "весна", 5: "весна", 6: "лето", 7: "лето", 8: "лето",
              9: "осень", 10: "осень", 11: "осень"}

if month == 1 or month == 2 or month == 12:
    print("Из списка: к этому месяцу относится время года", month_list[0])
elif month == 3 or month == 4 or month == 5:
    print("Из списка: к этому месяцу относится время года", month_list[1])
elif month == 6 or month == 7 or month == 8:
    print("Из списка: к этому месяцу относится время года", month_list[2])
elif month == 9 or month == 10 or month == 11:
    print("Из списка: к этому месяцу относится время года", month_list[3])
else:
    print("неверное значение")

print("Из словаря: к этому месяцу относится время года", month_dict.get(month))
