# Import of useful functions
from hex_skeleton import HexBoard
from search import dummy_eval, nextMove
from trueskill import Rating
from trueskill import rate_1vs1
import matplotlib.pyplot as plt
from eval import rem_hex

def match(boardsize, n, eval_f1, d1, eval_f2, d2, first_player):                        
    """ Used to let two AIs play against each other and compute their ratings after n number of games played"""
    r1 = Rating()                                           
    r2 = Rating()
    currentplayer = first_player                            # Red (eval_f1) = player 1 with rating r1
    count = 0                                               # Blue (evval_f2) = player 2 with rating r2    
    for i in range(1,n+1):                                  # n = number of matches
        board = HexBoard(boardsize)
        while board.check_win(board.RED) == False and board.check_win(board.BLUE) == False:       
            if currentplayer == 1:
                move1 = nextMove(eval_f1,board,d1,board.RED)
                makeMove(move1,board.RED,board)
                #board.print()
                currentplayer = 2
            if currentplayer == 2 and board.check_win(board.RED) == False and board.check_win(board.BLUE) == False:
                move2 = nextMove(eval_f2,board,d2,board.BLUE)
                makeMove(move2,board.BLUE,board)
                #board.print()
                currentplayer = 1
    
        if board.check_win(board.RED):          # After every game, the rating of each player is updated
            count = count + 1
            r1, r2 = rate_1vs1(r1, r2)        
        else:
            r2, r1 = rate_1vs1(r2, r1)
    print(count)                                # Count = is the number of wins of player 1 (red)
    return r1, r2


def experiment(boardsize, n,eval_f1,d1,eval_f2,d2):
    """ Used to plot the number of games against the ratings of each player. 
        After every game the first player is changed."""
    r1 = []                         # Ratings of player 1 (eval_f1)
    r2 = []                         # Ratings of player 2 (eval_f2)
    for n in range(1,n+1):                  
        if n%2 == 0:                # If n = even                              
            r = list(match(boardsize,n,eval_f1,d1,eval_f2,d2,1))                    
            r1.append(r[0].mu)
            r2.append(r[1].mu)
        else:
            r = list(match(boardsize,n,eval_f1,d1,eval_f2,d2,2))                    
            r1.append(r[0].mu)
            r2.append(r[1].mu)

    plt.plot(range(1,n+1),r1,label='Dijkstra(depth=3)')
    plt.plot(range(1,n+1),r2,label='Dijkstra(depth=4)')
    plt.xlabel('Number of games')
    plt.ylabel('μ value')
    plt.legend()
    plt.show()
    
    return r1,r2

# experiment(4,30,dummy_eval,3,rem_hex,3)
# experiment(4,30,dummy_eval,3,rem_hex,4)
# experiment(4,30,rem_hex,3,rem_hex,4)


