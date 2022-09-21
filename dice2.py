import random

coin_1 = 10
coin_2 = 10
while coin_1 > 0 and coin_2 > 0:
    if coin_1 == 0 or coin_2 == 0:
        break
    pirate_1 = random.randint(1, 6)
    pirate_2 = random.randint(1, 6)
    if pirate_1 > pirate_2:
        coin_1 += 1
        coin_2 -= 1
        print("Первый пират вбросил:", coin_1, "Второй пират выбросил:", coin_2)
        print("Выиграл первый пират")
    elif pirate_1 == pirate_2:
        coin_1 += 0
        coin_2 += 0
        print("Первый пират вбросил:", coin_1, "Второй пират выбросил:", coin_2)
        print("Ничья")
    else:
        coin_1 -= 1
        coin_2 += 1
        print("Первый пират вбросил:", coin_1, "Второй пират выбросил:", coin_2)
        print("Выиграл второй пират")
if coin_1 > coin_2:
        print("Победил первый пират")
else:
        print("Победил второй пират")
