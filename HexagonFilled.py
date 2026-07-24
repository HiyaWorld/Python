import turtle

length_line = 150
angle_of_turn = 60
turtle.pencolor("gold")
turtle.fillcolor("silver")
turtle.begin_fill()
turtle.bgcolor("grey")
for i in range(6):
    turtle.forward(length_line)
    turtle.left(angle_of_turn)
turtle.end_fill()
turtle.exitonclick()
