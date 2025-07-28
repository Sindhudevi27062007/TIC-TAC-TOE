import math

# Constants
HUMAN = 'O'
AI = 'X'
EMPTY = ' '

# Create board
def create_board():
    return [[EMPTY for _ in range(3)] for _ in range(3)]

# Print board
def print_board(board):
    print("\n".join([" | ".join(row) for row in board]))
    print()

# Check for win
def check_winner(board, player):
    # Rows, columns, diagonals
    for i in range(3):
        if all([cell == player for cell in board[i]]):
            return True
        if all([board[j][i] == player for j in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]):
        return True
    if all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

# Check for tie
def is_full(board):
    return all([cell != EMPTY for row in board for cell in row])

# Get empty cells
def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY]

# Minimax algorithm with Alpha-Beta pruning
def minimax(board, depth, is_maximizing, alpha, beta):
    if check_winner(board, AI):
        return 10 - depth
    if check_winner(board, HUMAN):
        return depth - 10
    if is_full(board):
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for i, j in get_empty_cells(board):
            board[i][j] = AI
            eval = minimax(board, depth + 1, False, alpha, beta)
            board[i][j] = EMPTY
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf
        for i, j in get_empty_cells(board):
            board[i][j] = HUMAN
            eval = minimax(board, depth + 1, True, alpha, beta)
            board[i][j] = EMPTY
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

# AI move
def ai_move(board):
    best_score = -math.inf
    move = None
    for i, j in get_empty_cells(board):
        board[i][j] = AI
        score = minimax(board, 0, False, -math.inf, math.inf)
        board[i][j] = EMPTY
        if score > best_score:
            best_score = score
            move = (i, j)
    if move:
        board[move[0]][move[1]] = AI

# Human move
def human_move(board):
    while True:
        try:
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter col (0-2): "))
            if board[row][col] == EMPTY:
                board[row][col] = HUMAN
                break
            else:
                print("Cell is already occupied. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Enter numbers between 0 and 2.")

# Main game loop
def play_game():
    board = create_board()
    print_board(board)
    while True:
        human_move(board)
        print_board(board)
        if check_winner(board, HUMAN):
            print("You win!")
            break
        if is_full(board):
            print("It's a tie!")
            break

        print("AI's turn:")
        ai_move(board)
        print_board(board)
        if check_winner(board, AI):
            print("AI wins!")
            break
        if is_full(board):
            print("It's a tie!")
            break

if __name__ == "__main__":
    play_game()
