# задача
# получить от пользователя число
# в зависимости от числа вывести на экран нужный текст


print("Вы находитесь на перекрестке трех дорог")
first = int(input("Введите 1 что бы пойти налево," "Введите 2 что бы пойти прямо," "Введите 3 что бы пойти направо "))
second=0
if first == 1:
    second=int(input(("Вы повернули налево и увидели банду разбойников, Введите 1 что бы сразиться с ними, Введите 2 что бы пройти мимо ")))
elif first == 2:
     second=int(input(("Вы прошли прямо и увидели огромный сундук. Введите 3 что бы подойти к нему, Введите 4 чтобы пройти мимо ")))
elif first == 3:
     second=int(input(("Вы прошли направо и увидели болото. Введите 5 что бы подойти ближе. Введите 6 что бы пройти мимо ")))
else:
    print("invalid number")

if second == 1:
    (input("Несмотря на все приложенные усилия разбойники оказались сильнее.Нажмите любую клавишу чтобы продолжить "))
elif second == 2:
    (input('Что то подсказывает вам, что это плохое решение. Вы проходите мимо в целости и сохранности. Нажмите любую клавишу чтобы продолжить '))
elif second ==3:
    (input('К вашему удивлению это не оказалось ловушкой, но сундук увы пуст. Нажмите любую клавишу чтобы продолжить.'))
elif second ==4:
    (input('Что то подсказывает вам, что это плохое решение. Вы проходите мимо в целости и сохранности. Нажмите любую клавишу чтобы продолжить'))
elif second ==5:
    (input("Подойдя к болоту вы не обнаруживаете ничего интересного. Нажмите любую клавишу чтобы продолжить"))
elif second ==6:
    (input('Что то подсказывает вам, что это плохое решение. Вы проходите мимо в целости и сохранности. Нажмите любую клавишу чтобы продолжить'))
else:
    print("invalid number")
print(input("Спасибо за игру нажмите любую клавишу чтобы выйти"))