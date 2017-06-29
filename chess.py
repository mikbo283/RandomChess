from graphics import *
from random import randint


class ChessPiece:
   def  __init__(self,pos,img,team,state):
       self.pos = pos
       self.img = img
       self.team = team
       self.state = state

       
       
#Dont touch Mike ;) 
def color_conf(i,j):

    def conf1():
        return j % 2 == 0

    def conf2():
        return j % 2 != 0

    if i % 2 == 0:
        return conf1

    else:
        return conf2
    


def main():

    x_size = 800
    y_size = 800
    win = GraphWin("chaosGame", x_size, y_size)
    inProgress = True

    A1 = ChessSquare(Point(400,400),Point(800,800),"foo","white")
    
    
    squares = []
    numbers = ["1","2","3","4","5","6","7","8"]
    letters  = ["A","B","C","D","E","F","G","H"]
    

    for i in range(0,8):
        for j in range(0,8):

            leftTopCorner = Point((x_size * i) / 8, (y_size * j / 8))
            rightBottomCorner = Point( (x_size * (i + 1)) / 8,  (y_size * (j + 1)) / 8 )

            conf = color_conf(i,j)
            
            if conf():
                squares.append(ChessSquare(leftTopCorner,rightBottomCorner,letters[i] + numbers[j],
                                           "white"))

            else :
                squares.append(ChessSquare(leftTopCorner,rightBottomCorner,letters[i] + numbers[j]
                                           ,"black"))

    for cs in squares:        
        cs.setFill(cs.color)
        cs.draw(win)
                           
    
    while inProgress:
        pass






















main()
