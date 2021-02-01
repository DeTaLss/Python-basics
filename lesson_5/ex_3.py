with open("salary.txt", "r", encoding="utf-8") as textf:
    file_dict = {line.split()[0]: int(line.split()[1]) for line in textf}
    print(f"Средний доход: {round(sum(file_dict.values()) / len(file_dict), 3)}")
    print(f"Сотрудники с окладом менее 20к: {[i[0] for i in file_dict.items() if i[1] < 20000]}")
