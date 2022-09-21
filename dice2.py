import random
coin1 = 10
coin2 = 10
while coin1 > 0 or coin2 > 0:
    pirate1 = random.randint(1,6)
    pirate2 = random.randint(1,6)
    if pirate1 > pirate2:
        coin1 += 1
        coin2 -= 1
        print("Выиграл первый пират")
    elif pirate1 == pirate2:
        coin1 += 0
        coin2 += 0
        print("Ничья")
    elif pirate1 < pirate2:
        coin1 -= 1
        coin2 += 1
        print("Выиграл второй пират")
    if coin1 == 0 or coin2 == 0:
        break
if coin1 > coin2:
        print("Победил первый пират")
else:
        print("Победил второй пират")