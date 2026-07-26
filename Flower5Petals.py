import turtle
turtle.pencolor("gold")
turtle.fillcolor("lavender")
turtle.begin_fill()

for i in range (5):
    turtle.circle(120 ,70)
    turtle.left(110)
    turtle.circle(120 ,70)
    turtle.left(180)

turtle.left(480)
turtle.end_fill()
turtle.pencolor("light green")
turtle.pensize(5)
turtle.circle(440 ,-90)


turtle.exitonclick()
