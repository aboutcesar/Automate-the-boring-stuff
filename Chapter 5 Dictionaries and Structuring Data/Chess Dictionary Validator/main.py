

board = {'e3': 'wking', 'c6': 'wqueen',
     'g2': 'bbishop', 'd2': 'bqueen', 'g3': 'bking',
     'a1': 'bpawn', 'm1': 'bpawn', 'c1': 'bpawn', 'd1': 'bpawn',
     'e1': 'bpawn', 'f1': 'bpawn', 'g1': 'bpawn', 'h1': 'bpawn',
     'e2': 'bpawn', 'a2': 'bpawn', 'z2': 'wpawn'}


def isValidChessBoard(board):

    wking, bking, wpieces, bpieces, wpawn, bpawn = 0,0,0,0,0,0
    spaces = []
    checkbol = True

#this makes the Board 1a-1h through 8a-8h
    for x in ('a','b','c','d','e','f','g','h'):
        for i in range(1,9):
            spaces.append(x+str(i))
        print(spaces)
#Begin Checking spaces and pieces
    for space, piece in board.items():

        # add the kings

        if piece == 'wking':
            wking += 1
        if piece == 'bking':
            bking += 1

        #add piece count
        if piece.startswith('w'):
            wpieces += 1

        if piece.startswith('b'):
            bpieces += 1

        #add the pawns
        if piece == "bpawn":
            bpawn += 1
        if piece == 'wpawn':
            wpawn += 1

        #check king count
    if wking != 1:
        print("White king != 1: " + str(wking))
        checkbol = False
    if bking > 1:
        print("Black king != 1: " + str(wking))
        checkbol = False

        #check pawn count
    if wpawn > 8:
        checkbol = False
        print("White pawn count too high, Invalid")
    if bpawn > 8:
        print("Black pawn count too high, Invalid")
        checkbol = False

        #check piece count
    if wpieces > 16:
        print("Total White pieces > 16")
        checkbol = False
    if bpieces > 16:
        print("Total White pieces > 16")
        checkbol = False

    #check if space is valid
    if space not in spaces:
        print('Space is wrong: ' + space + ' ' + piece)
        checkbol = False

    if checkbol:
        return True
    else:
        return False


print(isValidChessBoard(board))
