import turtle

turtle.shape("turtle")
turtle.speed(1)




#настройка
roof_side = math.sqrt((walls_width / 2) ** 2 + roof_height ** 2)
walls_width = 200
walls_height = 100
roof_height = 150
#стены
for i in range (4):
    turtle.forward(walls_width)
    turtle.left(90)
    turtle.forward(walls_height)
    turtle.left(90)


for i in range (3):
    turtle.forward(100)
    turtle.left(120)


turtle.right(90)
turtle.fd(100)
turtle.left(90)
turtle.forward(40)
turtle.left(90)
turtle.forward(40)
turtle.right(90)
turtle.forward(20)
turtle.right(90)
turtle.forward(40)

turtle.done()


