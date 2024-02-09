#!/usr/bin/python3
import sys

def is_valid(board, row, col, n):
    # Check if a queen can be placed in the given position
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def print_solution(board):
    # Convert board representation to the required format
    solution = [[i, board[i]] for i in range(len(board))]
    print(solution)

def solve_nqueens(board, row, n):
    # Recursive function to solve N-queens problem
    if row == n:
        # If all queens are placed, print the solution
        print_solution(board)
        return
    
    for col in range(n):
        if is_valid(board, row, col, n):
            board[row] = col
            solve_nqueens(board, row + 1, n)

def nqueens(n):
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: {} N".format(sys.argv[0]))
        sys.exit(1)

    try:
        # Convert command-line argument to integer
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Initialize the board with all elements set to -1
    board = [-1] * n
    solve_nqueens(board, 0, n)

if __name__ == "__main__":
    nqueens(0)
