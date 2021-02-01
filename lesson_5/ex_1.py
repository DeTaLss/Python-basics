with open("text_file.txt", "w", encoding="utf-8") as tex:
    while True:
        write = input("Введите данные: ")
        if not write:
            break
        print(write, file=tex)
