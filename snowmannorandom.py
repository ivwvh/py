import turtle as t
import random

t.shape("turtle")
t.speed(0)
t.colormode(255)
#контракт
#место
#радиус
#след. клруг в два раза меньше предидущего
# колво кругов
# цвет

turtle_position_x = int(input("Местонахождение черепахи (широта) "))
turtle_position_y = int(input("Местонахождение черепахи (высота) "))
radius = int(input("Введите радиус "))
circle_counter = int(input("Кол-во кругов "))
color = input("Цвет ")
t.pu()
t.goto(turtle_position_x, turtle_position_y)
t.pd()
t.color(color)
t.begin_fill()
for i in range (circle_counter):
    t.circle(radius)
    t.seth(90)
    t.pu()
    t.forward(radius * 2)
    radius = radius / 2
    t.right(90)
    t.pd()
t.end_fill()
t.done()