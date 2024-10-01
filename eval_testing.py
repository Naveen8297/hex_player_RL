from hex_skeleton import HexBoard
from eval import assign_val, dijkstra, rem_hex, board_graph
from search import getMoves, dummy_eval, unmakeMove, makeMove, alphabeta, nextMove
import time

#Tree
board = HexBoard(3)
board.place((2,0),board.BLUE)

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

print(alphabeta_test(rem_hex,board,depth=2))

# Performance evaluation

# Execution time of alphabeta with dijkstra evaluation for different board sizes
for i in range(2,7):
    board = HexBoard(i)
    print("Board size:")
    print(i)
    t1 = time.time()
    x = alphabeta(rem_hex,board,depth=2)
    t2 = time.time()
    delta = t2 - t1
    print(delta)

# Execution time of alphabeta with dijkstra evaluation for different search depths

board = HexBoard(6)
for d in range(1,5):
    print("Depth")
    print(d)
    t1 = time.time()
    x = alphabeta(rem_hex,board, depth=d)
    t2 = time.time()
    delta = t2 - t1
    print(delta)