def print_board(board):
    """Function to print the current board"""
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board, player):
    """Function to check if the player has won"""
    # Check rows, columns, and diagonals
    for i in range(3):
        if all([cell == player for cell in board[i]]):  # Check rows
            return True
        if all([board[j][i] == player for j in range(3)]):  # Check columns
            return True

    # Check diagonals
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True

    return False


def is_full(board):
    """Function to check if the board is full"""
    return all(cell != ' ' for row in board for cell in row)


def play_game():
    """Main function to control the game play"""
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        print_board(board)

        # Get player's move
        try:
            row = int(input(f"Player {current_player}, enter row (0-2): "))
            col = int(input(f"Player {current_player}, enter column (0-2): "))
        except ValueError:
            print("Invalid input. Please enter numbers between 0 and 2.")
            continue

        # Check if the move is valid
        if row not in range(3) or col not in range(3) or board[row][col] != ' ':
            print("Invalid move, try again.")
            continue

        # Make the move
        board[row][col] = current_player

        # Check for a winner
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        # Check for a tie
        if is_full(board):
            print_board(board)
            print("The game is a tie!")
            break

        # Switch players
        current_player = 'O' if current_player == 'X' else 'X'


if __name__ == "__main__":
    play_game()