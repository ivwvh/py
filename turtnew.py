import turtle as t
import math

t.shape("turtle")
t.speed(0)




#настройка

walls_width = int(input("Введите ширину стен ")) 
walls_height = int(input("Введите высоту стен ")) 
roof_height = int(input("Введите сторону "))
roof_side = math.sqrt((walls_width / 2) ** 2 + roof_height ** 2)
roof_angle =  math.degrees(math.atan(roof_height / (walls_width/2)))
walls_color = input("стены цвет")
roof_color = input('крыша цвет')
door_height = int(input('дверь высота'))
door_width = int(input("дверь ширина"))
t.fillcolor(walls_color)
t.begin_fill()
#стены
for i in range (2):
    t.forward(walls_width)
    t.right(90)
    t.forward(walls_height)
    t.right(90)
t.end_fill()

t.fillcolor(roof_color)
t.begin_fill()
t.left(roof_angle)
t.forward(roof_side)
t.right(roof_angle*2)
t.forward(roof_side)
t.setheading(180)
t.forward(walls_width)


t.setheading(270)
t.forward(walls_width)
t.left(90)
t.forward((walls_height/2) - (door_width/2))

t.done()




