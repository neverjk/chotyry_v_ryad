def create_board(rows, cols):
    board = [[" " for _ in range(cols)] for _ in range(rows)]
    return board


def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * (len(row) * 2 - 1))


def check_winner(board, player):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == player:
                if col <= len(board[0]) - 4:
                    if all(board[row][col + i] == player for i in range(4)):
                        return True
                if row <= len(board) - 4:
                    if all(board[row + i][col] == player for i in range(4)):
                        return True
                if row <= len(board) - 4 and col <= len(board[0]) - 4:
                    if all(board[row + i][col + i] == player for i in range(4)):
                        return True
                if row >= 3 and col <= len(board[0]) - 4:
                    if all(board[row - i][col + i] == player for i in range(4)):
                        return True
    return False


def drop_piece(board, col, player):
    for row in range(len(board) - 1, -1, -1):
        if board[row][col] == " ":
            board[row][col] = player
            return True
    return False


def main():
    rows = 6
    cols = 7
    board = create_board(rows, cols)
    player1 = "X"
    player2 = "O"
    current_player = player1

    while True:
        print_board(board)
        column = (
            int(input(f"Гравець {current_player}, оберіть стовпець (1-{cols}): ")) - 1
        )

        if not (0 <= column < cols):
            print("Неправильне значення стовпця. Спробуйте ще раз.")
            continue

        if not drop_piece(board, column, current_player):
            print("Цей стовпець заповнений. Спробуйте ще раз.")
            continue

        if check_winner(board, current_player):
            print_board(board)
            print(f"Гравець {current_player} переміг!")
            break

        if all(board[i][j] != " " for i in range(rows) for j in range(cols)):
            print_board(board)
            print("Нічия!")
            break

        current_player = player2 if current_player == player1 else player1


if __name__ == "__main__":
    main()
