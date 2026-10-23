import turtle
turtle.pencolor("gold")

radius1=120

for i in range (13):
    turtle.circle(radius1 ,180)
    radius1 = radius1 - 20
    if radius1 < 0 :
     turtle.pencolor("maroon")

turtle.exitonclick()
