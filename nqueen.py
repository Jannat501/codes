#!/usr/bin/env python
# coding: utf-8

# In[1]:


class TicTacToeState:
    def __init__(self, board, player):
        self.board = board
        self.player = player

    def is_goal_state(self):
        return self.check_winner() or self.is_draw()

    def is_draw(self):
        return len(self.get_valid_moves()) == 0

    def get_valid_moves(self):
        moves = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == "":
                    moves.append((i, j))
        return moves

    def check_winner(self):
        b = self.board
        for i in range(3):
            if b[i][0] == b[i][1] == b[i][2] != "":
                return b[i][0]
            if b[0][i] == b[1][i] == b[2][i] != "":
                return b[0][i]
        if b[0][0] == b[1][1] == b[2][2] != "":
            return b[0][0]
        if b[0][2] == b[1][1] == b[2][0] != "":
            return b[0][2]
        return None

    def make_move(self, move):
        i, j = move
        new_board = [row[:] for row in self.board]
        new_board[i][j] = self.player
        new_player = "O" if self.player == "X" else "X"
        return TicTacToeState(new_board, new_player)

    def calculate_cost(self):
        winner = self.check_winner()
        if winner == "X":
            return 1
        elif winner == "O":
            return -1
        else:
            return 0

    def get_moves(self):
        return [(i, j) for i in range(3) for j in range(3)]


# A* search algorithm
def tic_tac_toe_a_star(state):
    if state.is_goal_state():
        return []

    valid_moves = state.get_valid_moves()
    moves_scores = [(move, state.make_move(move).calculate_cost()) for move in valid_moves]
    moves_scores.sort(key=lambda x: x[1], reverse=True)

    for move, _ in moves_scores:
        next_state = state.make_move(move)
        optimal_moves = tic_tac_toe_a_star(next_state)
        if optimal_moves is not None:
            return [move] + optimal_moves

    return None


# Example game
initial_board = [["", "", ""], ["", "", ""], ["", "", ""]]
initial_player = "X"
initial_state = TicTacToeState(initial_board, initial_player)

optimal_moves = tic_tac_toe_a_star(initial_state)

if optimal_moves:
    print("Optimal Moves:")
    for i, move in enumerate(optimal_moves, start=1):
        print(f"Move {i}: Player {initial_player} moves to position {move[0]}, {move[1]}")
else:
    print("No optimal moves found. The game is either already won or a draw.")


# In[ ]:





# In[ ]:





# In[2]:


def AStar(startNode, stopNode):
    
    openSet = set([startNode])
    closeSet = set()
    dist = {}  # store distance from start node
    neighbour = {}  # Store adjacency nodes of all nodes
    
    dist[startNode] = 0
    neighbour[startNode] = None
    
    while len(openSet) > 0:
        currNode = None
        
        for v in openSet:
            if currNode is None or dist[v] + Heuristics(v) < dist[currNode] + Heuristics(currNode):
                currNode = v
        
        if currNode == stopNode or currNode not in graph:
            break
        else:
            for m, weight in GetNeighbour(currNode):
                if m not in openSet and m not in closeSet:
                    openSet.add(m)
                    neighbour[m] = currNode
                    dist[m] = dist[currNode] + weight
                else:
                    if dist[m] > dist[currNode] + weight:
                        dist[m] = dist[currNode] + weight
                        neighbour[m] = currNode
                        
                        if m in closeSet:
                            closeSet.remove(m)
                            openSet.add(m)
        
        openSet.remove(currNode)
        closeSet.add(currNode)
    
    if currNode is None:
        print('Path does not exist')
        return None
    
    if currNode == stopNode:
        path = []
        while neighbour[currNode] is not None:
            path.append(currNode)
            currNode = neighbour[currNode]
        path.append(startNode)
        path.reverse()
        print('Path Found: {}'.format(path))
        return path
    
    print('Path does not exist')
    return None

def GetNeighbour(currNode):
    if currNode in graph:
        return graph[currNode]
    else:
        return None

def Heuristics(n):
    hDist = {
        'A': 11,
        'B': 6,
        'C': 99,
        'D': 1,
        'E': 7,
        'G': 0,
    }
    return hDist[n]

graph = {
    'A': [('B', 2), ('E', 3)],
    'B': [('C', 1), ('G', 9)],
    'C': None,
    'E': [('D', 6)],
    'D': [('G', 1)]
}

AStar('A', 'G')


# In[ ]:





# In[ ]:





# In[3]:


class GraphColoring:
    def __init__(self, graph, num_colors):
        self.graph = graph
        self.num_colors = num_colors
        self.colors = [0] * len(graph)
        self.solution = None

    def is_safe(self, v, color):
        for i in range(len(self.graph)):
            if self.graph[v][i] == 1 and self.colors[i] == color:
                return False
        return True

    def backtrack(self, v):
        if v == len(self.graph):
            self.solution = self.colors.copy()
            return True

        for color in range(1, self.num_colors + 1):
            if self.is_safe(v, color):
                self.colors[v] = color
                if self.backtrack(v + 1):
                    return True
                self.colors[v] = 0

        return False

    def solve(self):
        if not self.backtrack(0):
            print("No solution exists.")
        else:
            print("Solution found:", self.solution)


graph = [
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 1, 0]
]
num_colors = 3

solver = GraphColoring(graph, num_colors)
solver.solve()


# In[31]:


def solve_n_queens(n):
    def backtrack(board, row, solutions):
        if row == n:
            solutions.append(board[:])
            return
        for col in range(n):
            if all(abs(board[i] - col) != row - i and col != board[i] for i in range(row)):
                board[row] = col
                backtrack(board, row + 1, solutions)

    solutions = []
    backtrack([None] * n, 0, solutions)
    return solutions

# Example usage
n = 4  # Number of queens and board size
solutions = solve_n_queens(n)

print("Number of solutions for",n,"-queens problem: ",len(solutions))
for i, solution in enumerate(solutions):
    print("Solution",(i+1),":")
    for row in solution:
        line = ['\t0'] * n
        line[row] = '\t1'
        print(''.join(line))


# In[30]:


def solve_n_queens(n):
    def backtrack(board,row,solutions):
        if row == n:
            solutions.append(board[:])
            return
        
        for col in range(n):
            if all((abs(board[i] - col) != row - i) and col != board[i] for i in range(row)):
                board[row] = col
                backtrack(board,row+1,solutions)
    solutions = []
    backtrack([None] * n,0,solutions)
    return solutions

n = 4
solutions = solve_n_queens(n)

print("Solutions are :",len(solutions))

for i,solution in enumerate(solutions):
    print("Solution :",(i+1))
    for row in solution:
        line = ['\t0']* n
        line[row] = '\t1'
        print("".join(line))


# In[34]:


def solve_n_queens(n):
    def backtrack(board,row,solutions):
        if row == n:
            solutions.append(board[:])
        for col in range(n):
            if all((abs(board[i] - col) != row - i) and board[i] != col for i in range(row)):
                board[row] = col
                backtrack(board,row+1,solutions)

    solutions = []    
    backtrack([None] * n,0,solutions)
    return solutions

n = 4
solutions = solve_n_queens(n)
print("Solution for ",n," queens problems are :",len(solutions))

for i,solution in enumerate(solutions):
    print("Solution :",(i+1))
    for row in solution:
        line = ['\t0'] * n
        line[row] = "\t1"
        print("".join(line))


# In[ ]:




