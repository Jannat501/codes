
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
n = 4  
solutions = solve_n_queens(n)

print("Number of solutions for",n,"-queens problem: ",len(solutions))
for i, solution in enumerate(solutions):
    print("Solution",(i+1),":")
    for row in solution:
        line = ['\t0'] * n
        line[row] = '\t1'
        print(''.join(line))


