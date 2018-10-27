import turtle as t
import datetime
def drawGap():
    t.penup()
    t.fd(5)
def drawLine(draw):
    drawGap()
    t.pendown() if draw else t.penup()
    t.fd(40)
    drawGap()
    t.right(90)
def drawDigit(d):
    drawLine(True) if d in [2,3,4,5,6,8,9] else drawLine(False)
    t.pencolor("red")
    drawLine(True) if d in [0,1,3,4,5,6,7,8,9] else drawLine(False)
    t.pencolor("blue")
    drawLine(True) if d in [0,2,3,5,6,8,9] else drawLine(False)
    t.pencolor("green")
    drawLine(True) if d in [0,2,6,8] else drawLine(False)
    t.pencolor("grey")
    t.left(90)
    drawLine(True) if d in [0,4,5,6,8,9] else drawLine(False)
    t.pencolor("darkgreen")
    drawLine(True) if d in [0,2,3,5,6,7,8,9] else drawLine(False)
    t.pencolor("gold")
    drawLine(True) if d in [0,1,2,3,4,7,8,9] else drawLine(False)
    t.pencolor("violet")
    t.left(180)
    t.penup()
    t.fd(20)
def drawDate(date):
    for i in date:
        if i == '-':
            t.write('年',font=("Arial", 18, "normal"))
            t.fd(40)
        elif i == '=':
            t.write('月',font=("Arial", 18, "normal"))
            t.fd(40)
        elif i == '+':
            t.write('日',font=("Arial", 18, "normal"))
        else:
            drawDigit(eval(i))
def main():
    t.setup(800,350,200,200)
    t.penup()
    t.fd(-350)
    t.pensize(5)
    drawDate(datetime.datetime.now().strftime('%Y-%m=%d+'))
    t.hideturtle()
main()
