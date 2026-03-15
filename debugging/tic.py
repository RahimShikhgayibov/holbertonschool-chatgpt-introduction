#!/usr/bin/python3

def print_board(board):
    for row in board:
        print(" | ".join(row))
        # Extended the dashes slightly so it perfectly matches the board width
        print("-" * 9)

def check_winner(board):
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def is_board_full(board):
    """Checks if there are any empty spaces left on the board."""
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    
    # Changed to an infinite loop so we can break out of it exactly when a game ends
    while True:
        print_board(board)
        
        try:
            row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
            col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))
            
            # Prevent IndexError by checking bounds before applying the move
            if row not in [0, 1, 2] or col not in [0, 1, 2]:
                print("Coordinates must be 0, 1, or 2. Try again.")
                continue
                
        except ValueError:
            # Prevent crashes if the user enters letters or symbols
            print("Invalid input! Please enter a valid number.")
            continue

        if board[row][col] == " ":
            board[row][col] = player
            
            # Check for a win IMMEDIATELY after the move, before swapping players
            if check_winner(board):
                print_board(board)
                print("Player " + player + " wins!")
                break
                
            # Check for a tie game
            if is_board_full(board):
                print_board(board)
                print("It's a draw!")
                break
            
            # Swap player only if the game is still going
            if player == "X":
                player = "O"
            else:
                player = "X"
        else:
            print("That spot is already taken! Try again.")

if __name__ == "__main__":
    tic_tac_toe()