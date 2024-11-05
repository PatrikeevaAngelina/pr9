import random
# Лотерейный билет
ticket = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25],
]
# Функция для выбора чисел
def us_selection():
    us_numbers = []
    for i in range(len(ticket)):
        while True:
            try:
                number = int(input(f"Выберите число из строки {i + 1} {ticket[i]}: "))
                if number in ticket[i]:
                    us_numbers.append(number)
                    break
                else:
                    print("Ошибка: число не из данной строки. Попробуйте снова.")
            except ValueError:
                print("Ошибка: введите корректное целое число.")
    return us_numbers
def rand_selection():
    rand_numbers = []
    for row in ticket:
        rand_numbers.append(random.choice(row))
    return rand_numbers
# Основная логика приложения
def lottery_app():
    print("Добро пожаловать в лотерею!")
    # Выбор пользователем
    us_numbers = us_selection()
    print("Ваши выбранные числа:", us_numbers)

    # Случайный выбор
    rand_numbers = rand_selection()
    print("Случайно выбранные числа:", rand_numbers)

    # Подсчет совпадений
    matches = set(us_numbers) & set(rand_numbers)
    print("Совпадения:", matches)
    print("Количество совпадений:", len(matches))


# Запуск приложения
lottery_app()