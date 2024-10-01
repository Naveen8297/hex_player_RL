import networkx as nx

def assign_val(board, player):
    """Used to assign the values of weights to the edges connecting the nodes"""

    if player == board.RED:  
        value = [[] for x in range(board.size)]
        for j in range(board.size):
            for i in range(board.size):
                
                if board.is_color((i,j),board.RED) == True:
                    value[j].append(0)       
                elif board.is_color((i,j),board.BLUE) == True:
                    value[j].append(99)
                elif board.is_color((i,j),board.EMPTY) == True:
                    value[j].append(1)
        return value
    
    elif player == board.BLUE:
        value = [[] for x in range(board.size)]
        for j in range(board.size):
            for i in range(board.size):
                
                if board.is_color((i,j),board.RED) == True:
                    value[j].append(99)       
                elif board.is_color((i,j),board.BLUE) == True:
                    value[j].append(0)
                elif board.is_color((i,j),board.EMPTY) == True:
                    value[j].append(1)
        
        return value

def board_graph(board, color):
    """To convert our HexBoard into a graph""" 
    if color == board.RED:
        v = assign_val(board, board.RED)       #Assign values of weights
        G = nx.Graph()       #Graph of type networkx
        G.add_node('T')
        G.add_node('D')       #Top and Down nodes for color red
   
        for j in range(board.size):
            for i in range(board.size):
                G.add_node((i,j))
            
        for j in range(board.size):
            for i in range(board.size):
                nb = board.get_neighbors((i,j))
                for n in nb:
                    G.add_edge((i,j), n, weight=v[j][i])        #Add nodes and edges with their respective weights
    
        for i in range(board.size):
            G.add_edge('T',(i,0), weight = v[0][i])
            G.add_edge('D',(i,board.size-1), weight = v[board.size-1][i])
        
        return G
    
    elif color == board.BLUE:
        v = assign_val(board, board.BLUE)
        G = nx.Graph()
        G.add_node('L')
        G.add_node('R')          #for color blue add the border nodes Left and Right
   
        for j in range(board.size):
            for i in range(board.size):
                G.add_node((i,j))
            
        for i in range(board.size):
            for j in range(board.size):
                nb = board.get_neighbors((i,j))
                for n in nb:
                    G.add_edge((i,j), n, weight=v[j][i])           #Add nodes and edges
    
        for i in range(board.size):
            G.add_edge('L',(0,i), weight = v[i][0])
            G.add_edge('R',(board.size-1,i), weight = v[i][board.size-1])
        
        return G

def dijkstra(board, color):
    """To calculate the shortest distance to the border for a particular color using Dijkstra's algorithm"""
    if color == board.RED:
        start = 'T'          
        goal = 'D'                #Top to bottom traversal for Red
        graph = board_graph(board, board.RED)
        
    elif color == board.BLUE:
        start = 'L'
        goal = 'R'                 #Left to right traversal for Blue
        graph = board_graph(board, board.BLUE)
     
    global shortest_distance
    shortest_distance = {}
    predecessor = {}
    unseenNodes = graph       #Mark all nodes as unvisited
    infinity = 99
    global path
    path = []
    for node in unseenNodes:
        shortest_distance[node] = infinity          #Distance to all nodes from source initialized to infinity
    shortest_distance[start] = 0          #Distance to source node is zero
    
    unseen = []
    for n in unseenNodes:
        unseen.append(n)
 
    while unseen:
        minNode = None
        for node in unseen:
            if minNode is None:
                minNode = node
            elif shortest_distance[node] < shortest_distance[minNode]:
                minNode = node          #Find the nearest neighbor
 
        for childNode in graph[minNode].keys():
            if graph[minNode][childNode]['weight'] + shortest_distance[minNode] < shortest_distance[childNode]:
                shortest_distance[childNode] = graph[minNode][childNode]['weight'] + shortest_distance[minNode]    #shortest distance
                predecessor[childNode] = minNode           
        x = minNode
        unseen.remove(minNode)
        
 
    currentNode = goal
    
    while currentNode != start:
        try:
            path.insert(0,currentNode)
            currentNode = predecessor[currentNode]
        except KeyError:
            #print('Path not reachable')
            break
    path.insert(0,start)
    if shortest_distance[goal] != infinity:
        #print('Shortest distance is ' + str(shortest_distance[goal]))
        #print('And the path is ' + str(path))
        sd = shortest_distance[goal]
    
        if color == board.RED:
            if board.board[path[len(path)-2]] == board.RED:
                return sd
            else:
                return sd-1
        
        elif color == board.BLUE:
            if board.board[path[len(path)-2]] == board.BLUE:
                return sd
            else:
                return sd-1                  #To remove the extra distance that has been added up 
    
    elif shortest_distance[goal] == infinity:
        return infinity

def rem_hex(board, color):
    """To calculate the final heuristic value of a board state and for a particular color"""    
    
    red = dijkstra(board, board.RED)
    blue = dijkstra(board, board.BLUE)
    
    if color == board.RED:
        heuristic = blue - red
    else: heuristic = red - blue
        
    return heuristic

