from turtle import Turtle

def isValidChessBoard(board):
    
    bking = 0
    wking = 0  
    bpieces = 0
    wpieces = 0
    ranks = ['a','b','c','d','e','f','g','h']
    pieces = ['pawn', 'rook', 'knight', 'bishop', 'king', 'queen']

# Rule: each player has at most 16 pieces, and only one of each colour king.
    for y in board.values():
        if y[:1] == 'w' and y[1:] in pieces:
            wpieces += 1
            if y == 'wking':
                wking += 1
        elif y[:1] == 'b' and y[1:] in pieces:
            bpieces += 1
            if y == 'bking':
                bking += 1
        else:
            print('Incorrect name:' + y)
            return False
    
    if bpieces > 16 or wpieces > 16 or bking != 1 or wking != 1:
        print('Incorrect pieces. Black has: ' + str(bpieces) + '. White has: ' + str(wpieces) + '.')
        print('White King count: ' + str(wking) + '.\n Black King count: ' + str(bking) + '.')
        return False

# Rule: pieces must be on squares 1a to 8h
    for z in board.keys():
        if int(z[0:1]) > 8 or int(z[0:1]) < 1 or z[1:2] not in ranks:
            print('Board value out of range: ' + z)
            return False

# All fine :)
    return True

startingBoard = {       # White pieces
                 '1a': 'wrook', '1b':'wknight', '1c':'wbishop', '1d':'wqueen',
                 '1e':'wking',  '1f':'wbishop','1g':'wknight', '1h':'wrook', 
                 '2a': 'wpawn','2b': 'wpawn', '2c': 'wpawn', '2d': 'wpawn', 
                 '2e': 'wpawn', '2f': 'wpawn', '2g': 'wpawn', '2h': 'wpawn',
                        # Black pieces
                 '8a': 'bpawn','7b': 'bpawn', '7c': 'bpawn', '7d': 'bpawn', 
                 '7e': 'bpawn', '7f': 'bpawn', '7g': 'bpawn', '7h': 'bpawn',
                 '8a': 'brook', '8b':'bknight', '8c':'bbishop', '8d':'bking',
                 '8e':'bqueen',  '8f':'bbishop','8g':'bknight', '8h':'brook',
                 }

if isValidChessBoard(startingBoard):
    print('The board is valid')