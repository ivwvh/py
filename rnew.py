import random
import os

#настройка
way_1 = True
way_2=True
way_3=True
game=True
scene=""
#имя
name=input('Введите имя')
if not name: name= "Илья"
#cycle
while game:
    if (way_1 or way_2 or way_3) and scene == "":
        print("Вы находитесь на перекрестке трех дорог")
        if way_1:
            print("Введите 1 что бы.")
        if way_2:
            print("Введите 2 что бы.")
        if way_3:
            print("Введите 3 что бы.")

        choice = input("Введите цифру ответа")
        scene = scene + choice

    #выбор1
    if way_1 and scene == "1":
        os.system("cls")
        print("Тестовый текст")
        print("Тестовый выбор 1")
        print("Тестовый выбор 2")

        choice = input("Выберите ответ")
        scene += choice



    #выбор2
    #выбор3

