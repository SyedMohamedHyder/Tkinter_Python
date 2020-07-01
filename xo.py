#!/c/Users/SYED/AppData/Local/Programs/Python/Python38/python

#-----------Global Variables-----------


import sys


board = ["-","-","-",
         "-","-","-",
         "-","-","-"]




def display_board():
    print("\n \n")
    print(board[0]+"|"+board[1]+"|"+board[2])
    print(board[3]+"|"+board[4]+"|"+board[5])
    print(board[6]+"|"+board[7]+"|"+board[8])


def main():

    display_board()
    print("\n \n press \"X\" to exit the game \n \n")
    while game_not_over():


       if not winner():
          x_chance()
          display_board()
       else:
          return "\n \n **************** Player \"O\" is Winner ****************\n \n"

       if not winner() and game_not_over():
          o_chance()
          display_board()
       elif winner():
          return "\n \n *************** Player \"X\" is Winner **************** \n \n"

    return "\n \n *************** (: DRAW THE MATCH :) ****************\n \n"


def x_chance():

    global board
    position=input("Where do you want to insert \"X\" : ")
    if position.lower()=="x":
       sys.exit("\n \n Game Stopped \n \n ")
      
    try:

       position=int(position)-1
       if position<len(board) and board[position]=="-" :
          board[position]="X"
       else :
          print ("\n Enter a valid position \n")
          x_chance()

    except:
       print ("\n Enter a valid position \n")
       x_chance()

def o_chance():

    global board
    position=input("Where do you want to insert \"O\" : ")

    if position.lower()=="x":
       sys.exit("\n \n Game Stopped \n \n ")
    try:
       position=int(position)-1
       if position<len(board) and board[position]=="-" :
          board[position]="O"
       else :
          print ("\n Enter a valid position \n")
          o_chance()
    except:
       print ("\n Enter a valid position \n")
       o_chance()



def game_not_over():


   return board.count("-")>=1 and board.count("-")<=9


def winner():

   return (board[0]!="-" and board[0]==board[1] and board[1]==board[2]) or (board[3]!="-" and board[3]==board[4] and board[4]==board[5]) or (board[6]!="-" and board[6]==board[7] and board[7]==board[8]) or (board[0]!="-" and board[0]==board[3] and board[3]==board[6]) or (board[1]!="-" and board[1]==board[4] and board[4]==board[7]) or (board[2]!="-" and board[2]==board[5] and board[5]==board[8]) or (board[0]!="-" and board[0]==board[4] and board[4]==board[8]) or (board[2]!="-" and board[2]==board[4] and board[4]==board[6])




print (main())
