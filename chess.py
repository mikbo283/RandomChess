from graphics import *
from random import randint


class ChessSquare(Rectangle):
   def __init__(self,corner1,corner2,chessPiece,color):
      Rectangle.__init__(self,corner1,corner2)
      self.chessPiece = chessPiece
      self.color = color

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


def set_up_board(squares,numbers,letters,win):
   for i in range(0,8):
        for j in range(0,8):

            leftTopCorner = Point((win.getWidth() * i) / 8, (win.getHeight() * j / 8))
            rightBottomCorner = Point( (win.getWidth() * (i + 1)) / 8,  (win.getHeight() * (j + 1)) / 8 )

            conf = color_conf(i,j)
            
            if conf():
               squares[letters[i] + numbers[j]] = ChessSquare(leftTopCorner,rightBottomCorner, None,"white")

            else :
                squares[letters[i] + numbers[j]] = ChessSquare(leftTopCorner,rightBottomCorner, None,"black")

   for key in squares:
      sq = squares[key]
      sq.setFill(sq.color)
      sq.draw(win)

def main():

    x_size = 800
    y_size = 800
    win = GraphWin("chaosGame", x_size, y_size)
    inProgress = True

    A1 = ChessSquare(Point(400,400),Point(800,800),"foo","white")
    
    squares = {}
    numbers = ["1","2","3","4","5","6","7","8"]
    letters  = ["A","B","C","D","E","F","G","H"]

    set_up_board(squares,numbers,letters,win)
    
    
    while inProgress:
        pass

     
main()
