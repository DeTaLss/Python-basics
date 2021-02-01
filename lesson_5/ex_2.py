with open("file_text2.txt", encoding="utf-8") as textf:
    lines = textf.readlines()
    for i, val in enumerate(lines, 1):
        words = len(val.split())
        print(f"В строке {i} содержится {words} слов")
