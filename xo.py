#!/c/Users/SYED/AppData/Local/Programs/Python/Python38/python

#-----------Global Variables-----------

board = ["-","-","-",
         "-","-","-",
         "-","-","-"]


def display_board():

    print(board[0]+"|"+board[1]+"|"+board[2])
    print(board[3]+"|"+board[4]+"|"+board[5])
    print(board[3]+"|"+board[4]+"|"+board[5])


def main():

    display_board()

    while True:


        x_chance()
        display_board()
        o_chance()
        display_board()


def x_chance():

    position=input("Where do you want to insert \"X\" : ")
    position=int(position)-1
    if position<len(board) and board[position]=="-" :
       board[position]="X"
    else :
       print ("Enter a valid position")
       x_chance()

def o_chance():

    position=input("Where do you want to insert \"O\" : ")
    position=int(position)-1
    if position<len(board) and board[position]=="-" :
       board[position]="O"
    else :
       print ("Enter a valid position")
       o_chance()

main()
