from random import randint

with open("file_text4.txt", "w+", encoding="utf-8") as textf:
    textf.write(" ".join([str(randint(27, 183)) for _ in range(35)]))
    textf.seek(0)
    print(sum(map(int, textf.readline().split())))
