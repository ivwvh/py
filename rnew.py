iimport random
import os

#настройка
way_1 = True
way_2=True
way_3=True
game=True
scene=""
#имя
name=input('Введите имя: ')
if not name: name= "Илья"
#cycle
while game:
    if (way_1 or way_2 or way_3) and scene == "":
        os.system("cls")
        scene = ""
        print("Вы находитесь на перекрестке трех дорог")
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
        print("Разбойники ")
        print("[1]Правильный выбор")
        print("[2]Неправильный выбор ")

        choice = input("Выберите ответ: ")
        if choice == "1" or choice== "2" :
            scene += choice
    #концовки для первого выбора
    if way_1 and scene == "11":
        input ("Концовка хорошая")
        scene = ""
        os.system("cls")
        way_1 = False

    if way_1 and scene == "12":
        input ("Концовка плохая")
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
