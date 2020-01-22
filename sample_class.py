'''Validation of Class Understanding'''
from turtle import *

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    '''Return concatenated string of x, y coordinates'''
    def __str__(self):
        variable = [str(self.x),str(self.y)]
        return ",".join(variable)
    
    '''Gets and returns the points X coordinate'''
    def getX(self):
        return(self.x)
    
    '''Gets and returns the points Y coordinate'''
    def getY(self):
        return(self.y)
    
    '''Resets the class object's X coordinate value'''
    def setX(self,x):
        self.x = x
        return None

    '''Resets the class object's Y coordinate value'''
    def setY(self,y):
        self.y = y
        return None

class Line:
    def __init__(self, startPoint, endPoint):
        self.startPoint = startPoint
        self.endPoint = endPoint

    '''Method to draw a line between two points'''
    def drawLine(self,t, color = "Black", size = 1):
        self.color = color
        self.size = size
        self.t = t
        self.t.penup()
        self.t.color(self.color)
        self.t.pensize(self.size)
        self.t.goto(self.startPoint.getX(),self.startPoint.getY())
        self.t.pendown()
        self.t.goto(self.endPoint.getX(),self.endPoint.getY())
        self.t.penup()
        self.t.home()

def main():
    t = Turtle()
    startPoint = Point(0,0)
    endPoint =  Point(50,50)
    line = Line(startPoint,endPoint)
    line.drawLine(t,"Silver","5")
    input()

if __name__ == "__main__": main()