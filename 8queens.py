N = 8

def is_safe(state, row, col):
    for r in range(row):
        c = state[r]
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True

def dfs_queens(state, row):
    if row == N:
        print_solution(state)
        return True

    for col in range(N):
        if is_safe(state, row, col):
            state[row] = col
            if dfs_queens(state, row + 1):
                return True
            state[row] = -1

    return False

def print_solution(state):
    for i in range(N):
        for j in range(N):
            if state[i] == j:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()

board = [-1] * N
dfs_queens(board, 0)
