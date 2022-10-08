import os
import random
player_name = input("Введите имя: ")
if not player_name: player_name = 'Илья'
shaman_event = True
tries = 5
shamans_number = random.randint(1, 5)
print(f"{player_name} встречает шамана")
print("Правила игры: Шаман загадывает случайное число от одного до пяти, ваша задача угадать какое число он загадал для этого у вас есть 5 попыток") 
while shaman_event and tries != 0:
      player_guess= int(input("Введите число: "))
      if player_guess != 0 and player_guess <= 5:
            if  player_guess < shamans_number:
                print("Это число меньше чем я загадал")
                tries -= 1
                print(f"Попыток осталось {tries}")
                input("Нажмите любую клавишу для продолжения")
                os.system("cls")
            elif player_guess > shamans_number:
                print("Это число больше того что я загадал")
                tries -= 1
                print(f"Попыток осталось {tries}")
                input("Нажмите любую клавишу для продолжения")
                os.system("cls")
            else:
                shamanevent = False
                print('Вы победили')

