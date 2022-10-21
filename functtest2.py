import turtle as t
import math

t.shape("turtle")
t.speed(1)

"""
walls_width = int(input("Введите ширину стен "))
walls_height = int(input("Введите высоту стен "))
roof_height = int(input("Введите сторону "))
roof_side = math.sqrt((walls_width / 2) ** 2 + roof_height ** 2)
roof_angle =  math.degrees(math.atan(roof_height / (walls_width/2)))
walls_color = input("стены цвет ")
roof_color = input('крыша цвет ')
door_height = int(input('дверь высота '))
door_width = int(input("дверь ширина "))
door_color = input("цвет двери ")
"""

def draw_house(walls_x,
    walls_y,
    walls_width,
    walls_height,
    walls_color,
    door_width,
    door_height,
    door_color,
    door_x,
    door_y):
    """

    x - левый нижний угол стены
    y - левый нижний угол стены
    walls_height - высота стен
    walls_wight - ширина стен
    door_x - левый нижний угол стены
    door_y - левый нижний угол стены
    door_width - ширина двери
    door_height - высота


    """
    door_x = ((walls_/2) - (door_width/2))
    door_y = door_x
    draw_walls(x, y, walls_height, walls_width, walls_color)
    draw_roof()
    draw_doors(door_width,door_height,door_color,door_x,door_y)

def draw_walls(x, y, walls_height, walls_width, walls_color):
    t.fillcolor(walls_color)
    t.begin_fill()
    for i in range (2):
        t.forward(walls_width)
        t.right(90)
        t.forward(walls_height)
        t.right(90)
    t.end_fill()


def draw_roof():
    print("Нарисовали крышу")


def draw_doors(door_width,door_height,door_color,door_x,door_y):
    print("Нарисовали двери")
    t.setheading(270)
    t.forward(walls_width)
    t.left(90)
    t.forward((walls_height/2) - (door_width/2))


draw_house(200,100, 100,100,"purple", 70, 90 )