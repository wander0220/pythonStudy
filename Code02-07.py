import turtle
import random

##def는 디파인 약자##
##함수선언부분##
def screenLeftClick(x,y):
    global r,g,b
    turtle.pencolor((r,g,b))
    turtle.pendown()
    turtle.goto(x,y)
    #turtle.circle(80)거북이 동글동글~!

def screenRightClick(x,y):
    turtle.penup()
    turtle.goto(x,y)
    

def screenMidClick(x,y):
    global r,g,b
    tSize=random.randrange(1,10)
    turtle.shapesize(tSize)
    r=random.random()
    g=random.random()
    b=random.random()


pSize=10
r,g,b=0.0, 0.0, 0.0

turtle.title('거북이로 그림그리기')
turtle.shape('turtle')
turtle.pensize(pSize)

turtle.onscreenclick(screenLeftClick,1)#마우스 왼쪽
turtle.onscreenclick(screenMidClick,2)
turtle.onscreenclick(screenRightClick,3)

turtle.done()
             


