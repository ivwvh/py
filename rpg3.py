# переменная для цикла
x = 0
# монеты и события
coins = 0
robbers = 0
chest = 0
swamp = 0

while x == 0:
# условие для концовки
    if coins == 3:
        x += 1
        break
    else:
        print("Вы находитесь на перекрестке трех дорог")

    first = int(input("Введите 1 что бы пойти налево. "
                      "Введите 2 что бы пойти прямо. "
                    "Введите 3 что бы пойти направо. "))
    second = 0
    if first == 1 and robbers != 1:
        second = int(input(("Вы повернули налево и увидели банду разбойников. "
                            "Введите 1 что бы сразиться с ними. "
                            "Введите 2 что бы пройти мимо. ")))
    elif first == 1 and robbers == 1:
        input(("Я уже тут был"))

    elif first == 2 and chest !=1:
        second = int(input(("Вы прошли прямо и увидели огромный сундук."
                            "Введите 3 что бы подойти к нему. "
                            "Введите 4 чтобы пройти мимо. ")))
    elif first == 2 and chest == 1:
        input(("Я уже тут был"))

    elif first == 3 and swamp != 1:
        second = int(input(("Вы прошли направо и увидели болото. "
                            "Введите 5 что бы подойти ближе. "
                            "Введите 6 что бы пройти мимо. ")))
    elif first == 3 and swamp == 1:
       input(("Я уже тут был"))
    else:
        print("invalid number")



# выбор с разбойниками
    if second == 1:
        (input("Несмотря на все приложенные усилия разбойники оказались сильнее. "
               "Нажмите любую клавишу чтобы продолжить "))
        break
    elif second == 2:
        coins += 1
        robbers +=1
        (input('Что то подсказывает вам, что это плохое решение. '
               'Вы проходите мимо в целости и сохранности. '
               "По дороге обратно вы находите монету. "
               'Нажмите любую клавишу чтобы продолжить '))
# выбор с сундуком
    elif second == 3:
        (input('Сундук оказался жилищем маленького гремлина, быстро выпрыгнув из сундука он нанес вам рану'
               ' увы не совместимую с жизнью. '
               'Нажмите любую клавишу чтобы продолжить.'))
        break
    elif second == 4:
        (input('Что то подсказывает вам, что это плохое решение.'
               'Вы проходите мимо в целости и сохранности.'
               "По дороге обратно вы находите монету. "
               'Нажмите любую клавишу чтобы продолжить'))
        coins += 1
        chest += 1
# выбор с болотом
    elif second == 5:
        (input("Подойдя к болоту вы не обнаруживаете ничего интересного. "
               " Нажмите любую клавишу чтобы продолжить "))
        break
    elif second == 6:
        (input('Что то подсказывает вам, что это плохое решение. '
               'Вы проходите мимо в целости и сохранности. '
               "По дороге обратно вы находите монету."
               'Нажмите любую клавишу чтобы продолжить '))
        coins += 1
        swamp += 1
    else:
        print("invalid number")
# концовка
while x == 1:
        ending = int(input("По дороге вы встречаете мудреца который предлагает вот показать путь отсюда."
                         "Всего за три монеты! "
                         "Нажмите 1 что бы заплатить мудрецу. "
                         "Нажмите 2 что бы пройти мимо. "))
        if ending == 1:
            input("Мудрец открывает вам неожиданную правду. "
                  "Все это время возравщаясь к перекрестку вы ходили окольными путями. "
                  "Что бы вернуться домой вам достаточно было просто развернуться назад......")
            break

        else:
            coins = 0
            robbers = 0
            chest = 0
            swamp = 0
            x = 0

            input("Мама учила вас не доврять незнакомцам. "
                  "Вы проходите мимо ничего не ответив. "
                  "Монеты магически пропадают из вашего кармана! "
                  "Кажется все повторяется....")
            


input("Спасибо за игру, нажмите любую клавишу чтобы выйти")
