# Import of useful functions and the HexBoard   
import random
from hex_skeleton import HexBoard

def getMoves(board):
    """ Find all possible/empty moves on the board and return it as a list"""
    moves = []
    
    for i in range(board.size):             # For every coordinate (i,j) on the board check if it is empty
        for j in range(board.size):
            if board.is_empty((i,j)) and board.game_over == False:
                moves.append((i,j))         # Add the coordinate to the list of moves
                
    return moves

def dummy_eval(board,color):
    """ Generates and returns a random integer number in the range from 1 to 10""" 
    r = random.randint(-20,20)
    return r

def unmakeMove(move, board):
    """ Sets the color of a coordinate (move) on the board to EMPTY"""
    board.board[move] = board.EMPTY

def makeMove(move, c, board):
    """ Sets the color of a coordinate (move) on the board to c (input)"""
    board.board[move] = c

board=HexBoard(2)

global v
v = {}

def alphabeta(eval_f, board, a=-99, b=99, depth=2, is_max=True, color = board.RED):
    """ Determines the optimal value, g, of a given board state"""
    
    if depth == 0 or board.check_win(board.BLUE) or board.check_win(board.RED):                  # At depth 0, we have reached a leafnode.  
        g = eval_f(board,color)
        return g                            # Therefore a random value is returned using the dummy_eval function
    
    elif is_max == True:                    # For a maximizing node (move):
        g = -99                             # Initialize the window             
        m = {}                              # v is a dictionary of all visited nodes and there corresponding value
        for c in getMoves(board):           # For every possible move on the board
            makeMove(c, color, board)               # Try the move
            #board.print() 
            n_g = alphabeta(eval_f,board, a, b, depth=depth-1, is_max=False, color = color)    # Find the value belonging to the move
            g = max(g, n_g)     
            m[n_g] = c                      # is_max is False, because the children of a maximizing node are min nodes
            unmakeMove(c,board)             # Unmake the move
            a = max(a, g)
            if g>=b:                        # If g, the value of the move, is bigger or equal to beta,
                break                       # the tree is cut off by breaking the loop
        v[depth] = m
        #print("max:", v)
        return g      
    
    elif is_max == False:                   # For a minimizing node, the same steps are taken:
        g = 99                      
        for c in getMoves(board):
            makeMove(c, board.get_opposite_color(color), board)
            #board.print()
            n_g = alphabeta(eval_f,board, a, b, depth=depth-1, is_max=True, color = color)
            g = min(g, n_g)
            unmakeMove(c,board)
            b = min(b, g)
            if a>=g:                        # If g is bigger or equal to alpha
                break                       # The tree is cutoff
        return g


def nextMove(eval_f,board,d=3,c=board.RED):
    """ Determines the next best move of a given board state, by extracting it 
        from the dictionary of visited nodes used in the alpha_beta function"""
    global v
    v = {}
    g = alphabeta(eval_f,board,depth=d,color=c)
    return v[d].get(g)

def main(boardsize):
    """ Provides a text-based user interface to play against the computer.
        The computer uses alpha_beta with random eval to find its next best move."""
        
    board = HexBoard(boardsize)
    option = input("If you want to play first, enter yes ; Else, enter no ：")
    if option == "yes":
        currentplayer = 1                   # 1 = human, BLUE
    elif option == "no":
        currentplayer = 2                   # 2 = computer, RED
    else:
        print("Wrong enter, you are playing first")
        currentplayer = 1
        
    board.print()
    while board.check_win(board.RED) == False and board.check_win(board.BLUE) == False:
        if currentplayer == 1:
            try:
                movex = input('Choose x coordinate of your move: ')
                movey = input ('Choose y coordinate of your move: ')
                move = (int(movex),int(movey))
                if board.is_empty(move):
                    makeMove(move,board.BLUE,board)
                    currentplayer = 2
                    board.print()
            except:
                print('This place is not empty, try again')
                continue

        if currentplayer == 2 and board.check_win(board.RED) == False and board.check_win(board.BLUE) == False:
            move = nextMove(dummy_eval,board,2,board.RED)
            print('Computer made a move ')
            makeMove(move,board.RED,board)
            board.print()
            currentplayer = 1
    
    if board.check_win(board.RED):
        print('You lose')
    if board.check_win(board.BLUE):
        print('You win')
