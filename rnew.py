import random
import os

#настройка
way_1 = True
way_2 = True
way_3 = True
game = True
scene = ""
battle = True

playerdamage = random.randint(1,10)
robberdamage = random.randint(1,5)
swordtype = ""
robberhp = 10
playerhp = 20
exp = 0
robbername = "Жран Борзой"


#выбор типа оружия
if playerdamage < 6:
    swordtype = "не заточенный"
if playerdamage < 10:
    swordtype == "плохо заточенный"
if playerdamage == 10:
    swordtype = "хорошо заточенный"

#имя

name = input('Введите имя: ')
if not name : name = "Илья"

#cycle
while game:

    if (way_1 or way_2 or way_3) and scene == "":
        os.system("cls")
        scene = ""
        print("Вы находитесь на перекрестке трех дорог")
        print(f"Возле одной из дорог вы видите {swordtype} меч ")
        if way_1:
            print("[1] Проехать налево.")
        if way_2:
            print("[2] Проехать прямо.")
        if way_3:
            print("[3] Проехать направо.")


        choice = input("Введите цифру ответа ")
        if choice == "1" or choice == "2" or choice =="3":
            scene = scene + choice

    #выбор1
    if way_1 and scene == "1":
        os.system("cls")
        print("Вы проходите лагеря разбойников")
        print("[1]Биться")
        print("[2]Не биться ")


        choice = input("Выберите ответ:")
        if choice == "1" and way_1 == True:
            print(f"Вас встретил {robbername} ")
            while battle:
                print(f"Жизни {robbername} :", robberhp)
                print("Ваши жизни", playerhp)
                input("Нажмите ENTER что бы сделать ход")
                playerhp = playerhp - robberdamage
                robberhp = robberhp - playerdamage
                print(f"{name} нанес: ", playerdamage)
                print(f"{robbername} нанес вам: ",robberdamage)
                input("Нажмите ENTER что бы продолжить")
                os.system("cls")
                if playerhp == 0 or playerhp < 0:
                    input("Вы проиграли")
                    scene = ""
                    break

                if robberhp == 0 or robberhp < 0:
                    input("Вы победили")
                    battle= False
                    way_1 = False
                    scene = ""

        if choice== "2":
            input("Вы решили пройти мимо")
            way_1 = False
            scene = ""



    if way_1 and scene == "12":
        input ("Вы решили пройти мимо них")
        scene = ""

    #выбор2
    if way_2 and scene == "2":
         os.system("cls")
         print("Сундук ")
         print (" [1] Правильный выбор  ")
         print (" [2] Неправильный выбор ")
         choice = input('Введите цифру ответа: ')
         if choice == "1" or choice== "2" :
            scene += choice
         if way_2 and scene == "21":
            input ("Концовка хорошая")
            scene = ""
            os.system("cls")
            way_2 = False

         if way_2 and scene == "22":
            input ("Концовка плохая")
            scene = ""

    #выбор3
    if way_3 and scene == "3":
         os.system("cls")
         print("Болото")
         print ("[1]Правильный выбор ")
         print ("[2]Неправильный выбор ")
         choice = input('Введите цифру ответа: ')
         if choice == "1" or choice== "3" :
            scene += choice
         if way_3 and scene == "31":
            input ("Концовка хорошая")
            scene = ""
            os.system("cls")
            way_3 = False

         if way_3 and scene == "32":
            input ("Концовка плохая ")
            scene = ""
    if way_1 == way_2 == way_3 == False:
        print("Все проехал")
        input("Конец игры")
        way_1 = True
        way_2 = True
        way_3 = True
        game = True
        scene = ""
