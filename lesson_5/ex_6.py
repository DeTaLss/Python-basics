with open("disciplines.txt", "r", encoding="utf-8") as textf:
    line = textf.readlines()
    for l in line:
        disp = "".join((i if i in "1234567890" else " ") for i in l)
        com_hour = [int(i) for i in disp.split()]
        print(f"{l.split()[0]} {sum(com_hour)}")
