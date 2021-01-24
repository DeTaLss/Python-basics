def int_func():
    for word in input("Введите слова из маленьких латинских букв через пробел: ").split():
        symbs = 0
        for symb in word:
            if 97 <= ord(symb) <= 122:
                symbs += 1
        print(word.title() if symbs == len(word) else "Вводить только маленькие латинские буквы")


int_func()
