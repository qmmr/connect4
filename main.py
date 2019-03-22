"""
Connect 4

For details, requirements and instructions see README.md file
"""
import os
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


def check_diagonals(board, player):
    # Tuples containing (row, position) of diagonal lines, bottom to top a.k.a. b2t
    b2t_diagonals = (
        ((3, 0), (2, 1), (1, 2), (0, 3)),
        ((4, 0), (3, 1), (2, 2), (1, 3), (0, 4)),
        ((5, 0), (4, 1), (3, 2), (2, 3), (1, 4), (0, 5)),
        ((5, 1), (4, 2), (3, 3), (2, 4), (1, 5), (0, 6)),
        ((5, 2), (4, 3), (3, 4), (2, 5), (1, 6)),
        ((5, 3), (4, 4), (3, 5), (2, 6)),
    )

    # Tuples containing (row, position) of diagonal lines, top to bottom a.k.a. t2b
    t2b_diagonals = (
        ((2, 0), (3, 1), (4, 2), (5, 3)),
        ((1, 0), (2, 1), (3, 2), (4, 3), (5, 4)),
        ((0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)),
        ((0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6)),
        ((0, 2), (1, 3), (2, 4), (3, 5), (4, 6)),
        ((0, 3), (1, 4), (2, 5), (3, 6)),
    )

    # Lists to hold rows from diagonals that can hold 4 or more tokens in the current board
    b2t_rows = []
    t2b_rows = []

    # Loops to create rows from diagonal lines
    for d in b2t_diagonals:
        new_row = []
        for row, pos in d:
            new_row.append(board[row][pos])

        b2t_rows.append(new_row)

    for d in t2b_diagonals:
        new_row = []
        for row, pos in d:
            new_row.append(board[row][pos])

        t2b_rows.append(new_row)

    return check_rows(b2t_rows, player) or check_rows(t2b_rows, player)


def check_winner(board, player):
    return check_rows(board=board, player=player) or check_cols(
        board=board, player=player) or check_diagonals(board=board, player=player)


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

    print("\n")


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
            # List comprehension that puts token in selected column if empty
            board[current_row] = [
                token if v == " " and i == selected_column else v for i, v in enumerate(row)]

            found_spot = True

    return board


def is_valid_column(column):
    return column in [1, 2, 3, 4, 5, 6, 7]


winner = None
turn_count = 0

# Main loop of the game
print("Welcome to connect 4!\n")
print("Let's begin!\n")
print("-" * 20, "\n")
while (winner is None):
    turn_count += 1
    print("Turn number {}!".format(turn_count))
    if current_player == 1:
        print("\nPlayer's one move!\n")
        print("-" * 20, "\n")
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
        print("\nPlayer's two move!\n")
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

    os.system('cls' if os.system == 'nt' else 'clear')
    print_board(global_board)


print("Game Over\n")

if winner == 1:
    print("Player #1 has won!")
elif winner == 2:
    print("Player #2 has won!")
else:
    print("It's a draw!")
