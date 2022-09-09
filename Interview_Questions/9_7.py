# Create simulated tic tac toe game. The game should consist of 2 players, 
# one using 'X' and the other 'O'. After each turn, player should mark a space 
# on the board according to their corresponding marker. Once a player successfully gets 3 pieces across 
# or diagonally, print who won. If there is no winner, print 'Tie game'.
# Print the position of the newly placed marker after each turn
# import random

import random
board = ['','','',
        '','','',
        '','','',]
x = 'x'
o = 'o'

turn = 0
setOfSpots = []
for i in range(len(board) -1):
        randomChoice = random.randint(0,len(board)-1)
        if board[randomChoice] == '' and turn % 2 == 0:
            board[randomChoice] = x
            turn += 1
            setOfSpots.append(randomChoice)
        elif board[randomChoice] == '' and randomChoice not in setOfSpots:
            board[randomChoice] = o
            turn += 1
            setOfSpots.append(randomChoice)
print(randomChoice)
print(setOfSpots)
print(board)



# def tictactoe():
#     turn = 0
#     for i in range(len(board) -1):
#         setOfSpots = []
#         randomChoice = random.randint(0,len(board)-1)
#         setOfSpots.append(randomChoice)
#         if board[randomChoice] == '' and turn % 2 == 0 and randomChoice not in setOfSpots:
#             board[randomChoice] = x
#             turn += 1
#         elif board[randomChoice] == '' and randomChoice not in setOfSpots:
#             board[randomChoice] = o
#             turn += 1
#         if board[0] == board[1] == board[2] and board[0] != '':    # check row wins
#             print('game over\n winner: %s' % board[0])
#             break
#         elif board[3] == board[4] == board[5] and board[3] != '-':
#             print('game over\n winner: %s' % board[3])
#         elif board[6] == board[7] == board[8] and board[6] != '-':
#             print('game over\n winner: %s' % board[6])
#         elif board[0] == board[3] == board[6] and board[0] != '-':  # check column wins
#             print('game over\n winner: %s' % board[0])
#         elif board[1] == board[4] == board[5] and board[1] != '-':
#             print('game over\n winner: %s' % board[1])
#         elif board[2] == board[5] == board[8] and board[2] != '-':
#             print('game over\n winner: %s' % board[2])
#         elif board[0] == board[4] == board[8] and board[0] != '-':  # check diagonal wins
#             print('game over\n winner: %s' % board[0])
#         elif board[6] == board[4] == board[2] and board[6] != '-':
#             print('game over\n winner: %s' % board[1])
#         if '' not in board and turn >= 9:
#             print('Tie game!')
#         print('\n')
#         print('turns: %d' % turn)
#         print(board[0] + ' | ' + board[1] + ' | ' + board[2])
#         print('----------')
#         print(board[3] + ' | ' + board[4] + ' | ' + board[5])
#         print('----------')
#         print(board[6] + ' | ' + board[7] + ' | ' + board[8])
# tictactoe()










# board1={"1":"-","2":"-","3":"-","4":"-","5":"-","6":"-","7":"-","8":"-","9":"-"}
# turns = 0
# playerOne = True
# board = ['', '', '',
#          '', '', '',
#          '', '', '']

# board = []

# def tictactoe():
#     playerChoice = int(input('Enter a number 0-8: '))
#     player1 = 'x'
#     player2 = 'o'

#     for i in range(0, len(board)-1):
#         if playerChoice >= 1 and playerChoice <= 9 and turns <= 9:
#             board[playerChoice] = player1
#             turns += 1
#         else:
            
        # choice = random.randint(0,len(board)-1)
        # if board[choice] == '' and turns <=9:
        #     board[choice] = 'x'
        #     turns += 1
        # else:
            
        # print(board)
# tictactoe()
            
        # board[i] = 'x'
            # print(choice)
            # print(board)
        # print(len(board))
        
        # board[choice]='x'
            # board.append(turn)
            # print(board)


# for XorO in range(10):

#     move = input()
    



# def togglePlayer(playerOne):
#     if(playerOne == True):
#         playerOne = False
#         return playerOne
#     elif(playerOne == False):
#         playerOne = True
#         return playerOne     

# playerOne=togglePlayer(playerOne)
# print(playerOne)
# print(togglePlayer(playerOne))
# print(playerOne)



    




# def rowWin():      # check row win
#     if board[0] == board[1] == board[2] and board[0] != '-':
#         winner = board[0]
#         return True
#     elif board[3] == board[4] == board[5] and board[3] != '-':
#         winner = board[3]
#         return True
#     elif board[6] == board[7] == board[8] and board[3] != '-':
#         winner = board[6]
#         return True

# def colWin():      # check column win
#     if board[0] == board[3] == board[6] and board[0] != '-':
#         winner = board[0]
#         return True
#     elif board[1] == board[4] == board[7] and board[1] != '-':
#         winner = board[1]
#         return True
#     elif board[2] == board[5] == board[8] and board[2] != '-':
#         winner = board[2]
#         return True

# def diagWin():     # checks diagonal win
#     if board[0] == board[4] == board[8] and board[0] != '-':
#         winner = board[0]
#         return True
#     elif board[6] == board[4] == board[2] and board[6] != '-':
#         winner = board[6]
#         return True

# def tie():
#     if turns == 9:
#         print("it's a tie!")

    

