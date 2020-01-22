from turtle import *

class objFun:
    def __init__(self,t):
        self.t = t
    
    def moveTurt(self):
        self.t.fd(100)
        self.t.home()
        return self.t

def main():
    t = Turtle()
    t.speed(1)
    temp = objFun(t)
    temp.moveTurt()
    t.rt(90)
    temp = objFun(t)
    temp.moveTurt()


    input()
    

if __name__ == "__main__": main()