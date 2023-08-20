def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("--" * 9)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(5):
        if all(board[row][col] == player for row in range(4)):
            return True

    if all(board[i][i] == player for i in range(5)) or all(board[i][2 - i] == player for i in range(5)):
        return True

    return False

def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

def main():
    board = [[' ' for _ in range(5)] for _ in range(5)]
    players = ['Abubakar', 'Aftab']
    current_player = players[0]

    while True:
        print_board(board)
        row = int(input(f"Player {current_player}, enter row (0-4): "))
        col = int(input(f"Player {current_player}, enter column (0-4): "))

        if board[row][col] == ' ':
            board[row][col] = current_player
        else:
            print("Cell already occupied. Try again.")
            continue

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = players[(players.index(current_player) + 1) % 2]

if __name__ == "__main__":
    main()
