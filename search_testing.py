from hex_skeleton import HexBoard
from search import getMoves, dummy_eval, unmakeMove, makeMove, alphabeta
import time
import matplotlib.pyplot as plt

#Tree 1
board = HexBoard(2)
board.place((0,0),board.BLUE)

global v
v = {}

def alphabeta_test(eval_f, board, a=-99, b=99, depth=2, is_max=True, color = board.RED):
    """ Determines the optimal value, g, of a given board state"""
    
    if depth == 0 or board.check_win(board.BLUE) or board.check_win(board.RED):                  # At depth 0, we have reached a leafnode.  
        g = eval_f(board,color)
        print(g)
        return g                            # Therefore a random value is returned using the dummy_eval function
    
    elif is_max == True:                    # For a maximizing node (move):
        g = -99                             # Initialize the window             
        m = {}                              # v is a dictionary of all visited nodes and there corresponding value
        for c in getMoves(board):           # For every possible move on the board
            makeMove(c, color, board)               # Try the move
            board.print() 
            n_g = alphabeta(eval_f,board, a, b, depth=depth-1, is_max=False, color = color)    # Find the value belonging to the move
            g = max(g, n_g)     
            m[n_g] = c                      # is_max is False, because the children of a maximizing node are min nodes
            unmakeMove(c,board)             # Unmake the move
            a = max(a, g)
            if g>=b:                        # If g, the value of the move, is bigger or equal to beta,
                break                       # the tree is cut off by breaking the loop
        v[depth] = m
        print("max:", v)
        return g      
    
    elif is_max == False:                   # For a minimizing node, the same steps are taken:
        g = 99                      
        for c in getMoves(board):
            makeMove(c, board.get_opposite_color(color), board)
            board.print()
            n_g = alphabeta(eval_f,board, a, b, depth=depth-1, is_max=True, color = color)
            g = min(g, n_g)
            unmakeMove(c,board)
            b = min(b, g)
            if a>=g:                        # If g is bigger or equal to alpha
                break                       # The tree is cutoff
        return g
    
print(alphabeta_test(dummy_eval,board,depth=3))

#Tree 2
board = HexBoard(3)
board.place((2,0),board.BLUE)

v = {}

print(alphabeta_test(dummy_eval,board,depth=2))

#Performance evaluation

def minimax(board,depth=3,is_max=True,color=board.RED):
    if depth == 0 or board.check_win(board.BLUE) or board.check_win(board.RED):
        g = dummy_eval(board,color)
        return g
    
    elif is_max == True:
        g = -99
        m = {}
        for c in getMoves(board):
            makeMove(c, color, board)
            n_g = minimax(board, depth=depth-1, is_max=False, color = color)
            g = max(g, n_g)
            unmakeMove(c,board)
            m[n_g] = c
        v[depth] = m
        return g      
    
    elif is_max == False:
        g = 99
        for c in getMoves(board):
            makeMove(c, board.get_opposite_color(color), board)
            g = min(g, minimax(board, depth=depth-1, is_max=True, color = color))
            unmakeMove(c,board)
        return g

#Execution time for different boardsizes
times1 = []
board = HexBoard(5)
for d in range(1,6):
    start_time = time.time()
    v = {}
    g = alphabeta(dummy_eval,board,depth=d)
    t = time.time() - start_time
    times1.append(t)

times2 = []
for d in range(1,6):
    start_time = time.time()
    v = {}
    g = minimax(board,depth=d)
    t = time.time() - start_time
    times2.append(t)

plt.plot(range(1,6),times1,label = 'Alpha-Beta')
plt.plot(range(1,6),times2, label = 'Minimax')
plt.ylabel('Time in s')
plt.xlabel('Search depths')
plt.legend()
plt.show()

##Execution time for different board sizes
times1 = []
for i in range(2,12):
    board = HexBoard(i)
    start_time = time.time()
    v = {}
    g = alphabeta(dummy_eval,board,depth=3)
    t = time.time() - start_time
    times1.append(t)

times2 = []
for i in range(2,12):
    board = HexBoard(i)
    start_time = time.time()
    v = {}
    g = minimax(board,depth=3)
    t = time.time() - start_time
    times2.append(t)
    
plt.plot(range(2,12),times1,label = 'Alpha-Beta')
plt.plot(range(2,12),times2, label = 'Minimax')
plt.ylabel('Time in s')
plt.xlabel('Board size')
plt.legend()
plt.show()
