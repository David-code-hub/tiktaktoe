import random
board = ['_','_','_',
         '_','_','_',
         '_','_','_']
player = 'x'
pos = 0
gameisActive = True
totalPlays = 0

def printBoard(board):
    print('TICK TAC TOE')
    print('--------------------')
    print(' | '+ board[0] + ' | ',board[1] + ' | ',board[2] + ' | ',)
    print('--------------------')
    print(' | ' + board[3] + ' | ', board[4] + ' | ', board[5] + ' | ',)
    print('--------------------')
    print(' | ' + board[6] + ' | ', board[7] + ' | ', board[8] + ' | ',)
    print('--------------------')

#choose play
def handlePlay(board):
    global player,pos,totalPlays,gameisActive
    if gameisActive == True:
        handlePosition()
        if pos >= 1 and pos <= 9:
            if board[pos -1] == '_':
                board[pos -1] = player
                totalPlays = totalPlays + 1
                handleCounter()
            else:
                if player == 'o':
                    player = 'x'
                    changePlayer(board)
                else:
                    print('position taken already!')
                    return
        else:
            print('Please enter  value lower 10 and more than 0')
            return

def handlePosition():
    global pos,player
    if player == 'o':
        pass
    else:
        pos = int(input('choose your play position : '))
def handleCounter():
    global totalPlays,gameisActive
    if totalPlays >= 9:
        gameisActive = False
        printBoard(board)
    else:
        print(f'total plays {totalPlays}')
        printBoard(board)
        changePlayer(board)

#change player
def changePlayer(board):
    global player,pos
    if player == 'x':
        player = 'o'
        pos = random.randint(1,9)
        handlePlay(board)
        # printBoard(board)
    else:
        player = 'x'

#who won?
def horizonalWin(board):
    global player,gameisActive
    if board[0] and board[1] and board[2] == player:
        gameisActive = False
        print(f'player {player} wins!')
    elif board[3] and board[4] and board[5] == player:
        gameisActive = False
        print(f'player {player} wins!')
    elif board[6] and board[7] and board[8] == player:
        gameisActive = False
        print(f'player {player} wins!')

def verticalWin(board):
    global player,gameisActive
    if board[0] and board[3] and board[6] == player:
        gameisActive = False
        print(f'player {player} wins!')
    elif board[1] and board[4] and board[7] == player:
        gameisActive = False
        print(f'player {player} wins!')
    elif board[2] and board[5] and board[8] == player:
        gameisActive = False
        print(f'player {player} wins!')

def diagonalWin(board):
    global player, gameisActive
    if board[0] and board[4] and board[8] == player:
        gameisActive = False
        print(f'player {player} wins!')
    elif board[2] and board[4] and board[6] == player:
        gameisActive = False
        print(f'player {player} wins!')


while gameisActive:
    horizonalWin(board)
    verticalWin(board)
    diagonalWin(board)
    handlePlay(board)