import json

with open("firmes.json", "w", encoding="utf-8") as jsf:
    with open("firm.txt", encoding="utf-8") as textf:
        profit = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in textf}
        common = [profit, {"Средняя выручка": round(sum([int(i) for i in profit.values() if int(i) > 0]) / len(
            [int(i) for i in profit.values() if int(i) > 0]))}]
    json.dump(common, jsf, ensure_ascii=False, indent=2)
