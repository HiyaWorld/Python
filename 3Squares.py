import turtle

length_line = 200
angle_of_turn = 90
turtle.pencolor("gold")

for i in range(12):
    turtle.forward(length_line)
    turtle.left(angle_of_turn)
    if i == 3 or i==7:
        turtle.left(120)
        if i == 3:
            turtle.pencolor("yellow")
        if i == 7:
            turtle.pencolor("silver")

turtle.exitonclick()
