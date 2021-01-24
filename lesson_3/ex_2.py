def user(name, surn, year, city, email, phone):
    print(f"Данные пользователя: имя: {name}, фамилия: {surn}, год рождения: {year}, город проживания: {city}, "
          f"email: {email}, телефон: {phone}")


user(name=input("Введите имя: "), surn=input("Введите фамилию: "), year=input("Введите год рождения: "),
     city=input("Введите город проживания: "), email=input("Введите email: "), phone=input("Введите номер телефона: "))
