# Python program to draw
# Spiral Square Outside In and Inside Out
# using Turtle Programming
from turtle import * 
wn = Screen()
wn.bgcolor("light green")
wn.title("Turtle")
sqr = Turtle()
sqr.color("blue")

def sqrfunc(size):
	for i in range(4):
		sqr.fd(size)
		sqr.left(90)
		size = size-5


def drawLineGoto(a,b):
    for i in range(0,100,10):
        up()
        goto(a[0]+i,a[1])
        pencolor('red')
        down()
        goto(b[0]+i,b[1])


def drawLineForward(a,ang,length):
    assert type(ang) == int
    assert type(length) == int
    up()
    goto(a)
    down()
    right(ang)
    forward(length)


def drawSquareFL(a,w):
    up()
    goto(a)
    down()
    for i in range(4):
        forward(w)
        left(90)
        
    
def drawTri(a,b,c):
    up()
    goto(a)
    down()
    goto(b)
    goto(c)
    goto(a)
    

def drawSquareG(c,w):
    up()
    goto(c)
    #setheading(90)
    down()
    goto(c[0]+w,c[1])
    goto(c[0]+w,c[1]+w)
    goto(c[0],c[1]+w)
    goto(c[0],c[1])


def drawEqTriFL(c,ang,L):
    up()
    goto(c)
    down()
    right(ang)
    forward(L)
    left(120)
    forward(L)
    left(120)
    forward(L)


def drawFilledSquareFR(a,w):
    up()
    goto(a)
    down()
    for i in range(4):
        forward(w)
        right(90)
        

drawLineGoto((100,100),(100,150))
pencolor('black')
drawLineForward((1,1),0,100)
pencolor('green')
drawLineForward((10,10),-45,125)
#setheading(0)
#drawLineForward((0,0),-90,100)
#setheading(0)
#drawLineForward((0,0),90,100)
color('magenta')
#begin_fill()
setheading(90)
drawSquareFL((-10,20),50)
#end_fill()
color('blue')
#begin_fill()
setheading(90)
drawTri((-50,-50),(-20,-50),(-10,-20))
#end_fill()
color('red')
setheading(90)
drawSquareG((-30,50),10)
color('yellow')
setheading(90)
begin_fill()
drawEqTriFL((-30,-150),20,50)
end_fill()
#color('cyan')
#setheading(90)
#drawFilledSquareFR((-30,30),10)
hideturtle()

x = 246
for i in range(12):
	sqrfunc(x-20*i)

sqr.hideturtle()

done()
