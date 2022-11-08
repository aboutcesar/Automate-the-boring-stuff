import sys

Empty_Space = "."
player_X    = "x"
player_O    = "O"

board_width     = 7
board_height   = 6
columns_Labels = ("1","2","3","4","5","6","7")

#templete for displaying the board
board_Templete = """
   1234567
  *.......*
|{}{}{}{}{}{}|
|{}{}{}{}{}{}|
|{}{}{}{}{}{}|
|{}{}{}{}{}{}|
|{}{}{}{}{}{}|
|{}{}{}{}{}{}|
  *.......*
  """

def main():
    '''Runs only one round of the connect 4'''
    print("4 in a row: ")
    #new board and player turn 
    board = getNewBoad()
    player_turn = player_X

    while True:
        print(board)
        

    

def getNewBaord():
    #creates a fresh clean board using global columns and width
    newboard = {}
    for column_index in board_width:
        for row_index in board_height:
            newboard[(column_index, row_index)] = Empty_Space
    return newboard

def getPlayerMove(playerTurn, board):
    while True:
        #ask player to enter a column to place the disk
        print(f'Player {playerTurn}, Enter 1 to {board_width}, or Quit to end: ')
        response = input()

        if str.lower(response) == 'quit':
            print("thanks for playing")
            sys.exit()
        if str(response) not in column labels:
            print("That is not a valid column")
            print(f'Enter a column from 1 to {board_width')

        column_index = int(response) - 1
        if board[(column_index, 0)] != Empty_Space:
            print("This column is full. Please choose another column")
            continue # Finishes and goes again to ask the player
        for row_index in range(board_height - 1, -1, -1): # 
            if board[(column_index, row_index)] == Empty_Space:
                return(column_index, row_index)]
            
        

def isWinner(playerTile, board):
#need to check diagnol, vertical, and horizontal
    #vertical
    for column_index in range(board_width):
        for row_index in range(board_Height-3): #3 because we are only checking 4 places and there are 7 rows
            place1 == board[(column_index,row_index)]
            place2 == board[(column_index,row_index+1)]
            place3 == board[(column_index,row_index+2)]
            place4 == board[(column_index,row_index+3)]

            if place1 = place2 = place3 = place4=playerTile:
                return True
    # Horizontal
    for column_index in range(board_width-3):
        for row_index in range(board_Height): 
            place1 == board[(column_index,row_index)]
            place2 == board[(column_index+1,row_index)]
            place3 == board[(column_index+2,row_index)]
            place4 == board[(column_index+3,row_index)]

            if place1 = place2 = place3 = place4=playerTile:
                return True

    #diagnal to the right
    for column_index in range(board_width-3):
        for row_index in range(board_Height-3):
            place1 == board[(column_index,row_index)]
            place2 == board[(column_index+1,row_index+1)]
            place3 == board[(column_index+2,row_index+2)]
            place4 == board[(column_index+3,row_index+3)]

            if place1 = place2 = place3 = place4=playerTile:
                return True

    #diagnal to the left
     
            place1 == board[(column_index+3,row_index)]
            place2 == board[(column_index+2,row_index+1)]
            place3 == board[(column_index+1,row_index+2)]
            place4 == board[(column_index,row_index+3)]

            if place1 = place2 = place3 = place4=playerTile:
                return True
    return False

    
    
def isFull(board):
    #is the board full? return false 
    for column_index in range(board_width-1):
        for row_index in range(board_height-1,-1,-1):
            if board[(column_index, row_index) == Empty_space:
                     return False 
    return True 

def displayBoard():
    pass


if __name__ == "__main__":
    main()

                     
