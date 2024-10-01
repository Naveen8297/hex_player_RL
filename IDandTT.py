import time
from search import getMoves, dummy_eval, unmakeMove, makeMove
from hex_skeleton import HexBoard
from eval import rem_hex

board = HexBoard(3)

global table
table = {}

def board_state(board):
    state = []
    for x in range(board.size):
        for y in range(board.size):
            state.append(x)
            state.append(y)
            state.append(board.get_color((x,y)))
    s = "".join(map(str,state))
    return s


def alpha_TT(eval_f,board, a=-99, b=99, depth=2, is_max=True, color = board.RED):   
    if board in table.keys():
        g = table[board_state(board)]
        return g
    
    if depth == 0 or board.check_win(board.BLUE) or board.check_win(board.RED):
        g = eval_f(board,color)
        table[board_state(board)] = g
        return g
    
    elif is_max == True:
        g = -99
        global v
        m = {}
        for c in getMoves(board):
            makeMove(c, color, board)
            n_g = alpha_TT(eval_f,board, a, b, depth=depth-1, is_max=False, color = color)
            g = max(g, n_g)
            m[n_g] = c
            table[board_state(board)] = n_g
            #print("max:",v)
            #board.print()
            #print(n_g)
            unmakeMove(c,board)
            a = max(a, g)
            if g>=b:
                break
        #print(table)
        v[depth] = m
        return g      
    elif is_max == False:
        g = 99
        for c in getMoves(board):
            makeMove(c, board.get_opposite_color(color), board)
            n_g = alpha_TT(eval_f,board, a, b, depth=depth-1, is_max=True, color = color)
            table[board_state(board)] = n_g
            g = min(g, n_g)
            #board.print()
            #print(n_g)
            unmakeMove(c,board)
            b = min(b, g)
            if a>=g:
                break
        return g
    

def iterativedeepening(board):
    d = 1
    t = time.time()
    while time.time() < t+5:
        global v
        v = {}
        g = alpha_TT(rem_hex,board, depth=d)
        move = v[d].get(g)
        d = d + 1
    return move
