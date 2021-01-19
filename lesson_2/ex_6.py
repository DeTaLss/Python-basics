products = []
various = {"название": "", "цена": "", "количество": "", "еденица изм": ""}
analytics = {"название": [], "цена": [], "количество": [], "еденица изм": []}
num = 0

while True:
    if input("Для завершения введите 'конец', для продолжения нажмите 'enter': ") == "конец":
        break
    num += 1
    various = various.copy()
    for val in various:
        ent = input(f"Введите значение товара '{val}': ")
        various[val] = int(ent) if val == "цена" or val == "количество" else ent
        analytics[val].append(various[val])
    products.append((num, various))
    print(f"Структура товаров{products}")
    print(f"Аналитика по товарам: ")
    for key, value in analytics.items():
        print(key, value)
