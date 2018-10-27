import turtle as t
import datetime
a=0
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
    global a
    drawLine(True) if d in [2,3,4,5,6,8,9] else drawLine(False)
    drawLine(True) if d in [0,1,3,4,5,6,7,8,9] else drawLine(False)
    drawLine(True) if d in [0,2,3,5,6,8,9] else drawLine(False)
    drawLine(True) if d in [0,2,6,8] else drawLine(False)
    t.left(90)
    drawLine(True) if d in [0,4,5,6,8,9] else drawLine(False)
    drawLine(True) if d in [0,2,3,5,6,7,8,9] else drawLine(False)
    drawLine(True) if d in [0,1,2,3,4,7,8,9] else drawLine(False)
    t.left(180)
    t.penup()
    t.fd(20)
    a=a+1
    if a == 1:
        t.pencolor("green")
    if a == 2:
        t.pencolor("red")
    if a == 3:
        t.pencolor("grey")
    if a == 4:
        t.pencolor("darkgreen")
    if a == 5:
        t.pencolor("gold")
    if a == 6:
        t.pencolor("violet")
    if a == 7:
        t.pencolor("purple")
    if a == 8:
        t.pencolor("orange")
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
