rus_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

with open("file_text3new.txt", "w", encoding="utf-8") as new:
    with open("file_text3.txt", encoding="utf-8") as textf:
        new.writelines([line.replace(line.split()[0], rus_dict.get(line.split()[0])) for line in textf])
