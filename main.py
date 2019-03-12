"""
Connect 4

For details, requirements and instructions see README.md file
"""

current_player = 1
empty_token = " "
player1_token = 'X'  # u'\u26aa'
player2_token = 'O'  # u'\u26ab'

global_board = [
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
]


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
            # print(idx)
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
        else:
            print("row {} col {} is taken!".format(
                current_row, selected_column))
            continue

    # print("board after placing the token", board)

    return board


def is_valid_column(column):
    return column in [1, 2, 3, 4, 5, 6, 7]


winner = None
turn_count = 0

while (winner == None):
    turn_count += 1
    print("Turn number {}!".format(turn_count))
    if current_player == 1:
        print("Player's one move!\n")
        col_number = int(input("Please enter column number: "))

        if is_valid_column(col_number):
            # Fill the global board with player one's token
            global_board = drop_token(global_board, col_number)
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
            # End player two's turn
            current_player = 1
        else:
            print("Wrong column, please choose number between 1-7")

    print_board(global_board)
