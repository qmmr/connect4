"""
Connect 4

For details, requirements and instructions see README.md file
"""
from itertools import groupby

current_player = 1
empty_token = " "
player1_token = 'X'  # u'\u26aa'
player2_token = 'O'  # u'\u26ab'

global_board = [
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],  # 0
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],  # 1
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],  # 2
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],  # 3
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],  # 4
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],  # 5
]


def check_rows(board, player):
    token = player1_token if current_player == 1 else player2_token

    for row_idx in range(len(board) - 1, -1, -1):
        # Group adjacent items into lists
        grouped = [list(v) for k, v in groupby(board[row_idx])]

        # Create a dictionary from grouped values
        obj = {key: val for (key, val) in [tuple(
            [v[0], len(v)]) for v in grouped]}

        # Check if player has 4 tokens
        if token in obj and obj[token] == 4:
            return True

    return False


def check_cols(board, player):
    # Convert rows to columns
    flipped_board = [list(val) for val in list(zip(*board))]

    return check_rows(flipped_board, player)


def check_winner(board, player):
    return check_rows(board=board, player=player) or check_cols(
        board=board, player=player)

    return won


def print_board(board):
    # Loop over each column and print column numbers
    for idx in range(1, 8):
        if idx != 7:
            print("[{}]".format(idx), end="")
        else:
            print("[{}]".format(idx))

    # Loop rows
    for row in board:
        # Draw column
        for idx, col in enumerate(row):
            if idx != 6:
                print("[{}]".format(col), end="")
            else:
                print("[{}]".format(col))


def drop_token(board, selected_column):
    selected_column = selected_column - 1
    token = player1_token if current_player == 1 else player2_token
    found_spot = False
    # Starting from the bottom row going up
    for current_row in range(5, -1, -1):
        # Exit loop when token is placed
        if found_spot:
            break

        row = board[current_row]

        # Check if col in current row is empty
        if row[selected_column] == ' ':
            # List comprehension that puts token in selected column if it's empty
            board[current_row] = [
                token if val == empty_token and idx == selected_column else val for idx, val in enumerate(row)]

            found_spot = True

    return board


def is_valid_column(column):
    return column in [1, 2, 3, 4, 5, 6, 7]


winner = None
turn_count = 0

while (winner is None):
    turn_count += 1
    print("Turn number {}!".format(turn_count))
    if current_player == 1:
        print("Player's one move!\n")
        col_number = int(input("Please enter column number: "))

        if is_valid_column(col_number):
            # Fill the global board with player one's token
            global_board = drop_token(global_board, col_number)
            if check_winner(global_board, current_player):
                winner = current_player
            # End player one's turn
            current_player = 2
        else:
            print("Wrong column, please choose number between 1-7")

    else:
        print("Player's two move!\n")
        col_number = int(input("Please enter column number: "))

        if is_valid_column(col_number):
            # Fill the global board with player two's token
            global_board = drop_token(global_board, col_number)
            if check_winner(global_board, current_player):
                winner = current_player
            # End player two's turn
            current_player = 1
        else:
            print("Wrong column, please choose number between 1-7")

    print_board(global_board)


print("The game has ended!\n")

if winner == 1:
    print("Player #1 has won!")
elif winner == 2:
    print("Player #2 has won!")
else:
    print("It's a draw!")
