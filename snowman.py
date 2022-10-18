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
while True:
    turtle_position_x = random.randint(-200, 200)
    turtle_position_y = random.randint(-200, 200)
    radius = random.randint(10, 50)
    circle_counter = random.randint(3,7)
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)

    t.pu()
    t.goto(turtle_position_x, turtle_position_y)
    t.pd()
    t.color(red,green,blue)
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