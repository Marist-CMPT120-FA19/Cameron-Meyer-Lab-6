#Cameron Meyer
#Cameron.meyer2@marist.edu
from graphics import *
def drawlightbody(x, y, length, width):
	win= GraphWin()
	b=Rectangle(Point(x,y),Point(length,width))
	b.setOutline("black")
	b.setFill("white")
	b.draw(win)
	
def drawlamp(color,x,y, radius):
	light= Circle(Point(x,y), radius)
	light.setOutline("black")
	light.setFill(color)
	light.draw(win)

def drawTrafficlight(x,y):
        drawlightbody(x, y, 150, 175)
        drawlamp("red"100, 50, 20)
        drawlamp("yellow"100,100, 20)
        drawlamp("green"100, 150, 20)



drawTrafficlight(150,150)

