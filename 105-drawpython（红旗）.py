#zhuyi柱.py
import turtle
turtle.setup(650, 600, 150, 150)
turtle.penup()
turtle.pencolor("black")
turtle.pensize(1)
turtle.seth(60)
turtle.fd(-330)
turtle.pendown()
turtle.seth(90)
turtle.fd(500)
turtle.seth(-90)
turtle.circle(5, 180)
turtle.seth(-90)
turtle.fd(500)
turtle.penup()
turtle.fd(-500)
#顶部
turtle.seth(90)
turtle.pendown()
turtle.pensize(2)
turtle.circle(5, 180)
turtle.seth(0)
turtle.pensize(1)
turtle.fd(5)
turtle.penup()
turtle.seth(90)
turtle.fd(50)
turtle.pendown()
turtle.seth(-130)
turtle.fd(15)
turtle.seth(-80)
turtle.fd(40)
turtle.seth(0)
turtle.fd(8)
turtle.seth(80)
turtle.fd(40)
turtle.seth(140)
turtle.fd(16)
turtle.penup()
turtle.seth(-90)
turtle.fd(48)
#红旗
turtle.pendown()
turtle.pencolor("red")
turtle.fillcolor("red")
turtle.begin_fill()
turtle.seth(0)
turtle.fd(8)
turtle.seth(-90) 
turtle.fd(220)
turtle.seth(180)
turtle.fd(2)
turtle.seth(0)
turtle.fd(8)
turtle.seth(90)
turtle.fd(5)
turtle.seth(0)
turtle.fd(350)
turtle.seth(90)
turtle.fd(210)
turtle.seth(180)
turtle.fd(355)
turtle.end_fill()
#星星  
turtle.penup()          
turtle.seth(-90)
turtle.fd(40)
turtle.seth(0)
turtle.fd(15)
turtle.pendown()
turtle.pencolor("yellow")
turtle.fillcolor("yellow")
turtle.begin_fill()
for i in range(5):
    turtle. forward(55)
    turtle.right(144)
turtle.end_fill()
turtle.seth(18)
turtle.penup()
turtle.fd(65)
turtle.seth(-20)
turtle.circle(-30, 150)
turtle.seth(10)
turtle.circle(30, 150)
turtle.seth(60)
turtle.pendown()
turtle.pencolor("yellow")
turtle.fillcolor("yellow")
turtle.begin_fill()
for i in range(5):
    turtle. forward(15)
    turtle.right(144)
turtle.end_fill()
turtle.penup()
turtle.seth(-20)
turtle.circle(-30, 50)
turtle.pendown()
turtle.seth(30)
turtle.pencolor("yellow")
turtle.fillcolor("yellow")
turtle.begin_fill()
for i in range(5):
    turtle. forward(15)
    turtle.right(144)
turtle.end_fill()
turtle.penup()
turtle.seth(-70)
turtle.circle(-30, 50)
turtle.pendown()
turtle.seth(0)
turtle.pencolor("yellow")
turtle.fillcolor("yellow")
turtle.begin_fill()
for i in range(5):
    turtle. forward(15)
    turtle.right(144)
turtle.end_fill()
turtle.penup()
turtle.seth(-100)
turtle.circle(-30, 50)
turtle.pendown()
turtle.seth(-30)
turtle.pencolor("yellow")
turtle.fillcolor("yellow")
turtle.begin_fill()
for i in range(5):
    turtle. forward(15)
    turtle.right(144)
turtle.end_fill()
turtle.penup()


