"""
Connect 4

For details, requirements and instructions see README.md file
"""

current_player = 1
player1_color = u'\u26aa'
player2_color = u'\u26ab'

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

    # Loop over each column
    for row in board:
        for idx, col in enumerate(row):
            # print(idx)
            if idx != 6:
                print("[{}]".format(col), end="")
            else:
                print("[{}]".format(col))


def drop_token(board, selected_column):
    print(board)
    return board


winner = None
turn_count = 0

while (winner == None):
    turn_count += 1
    print("Turn number {}!".format(turn_count))
    if current_player == 1:
        print("Player's one move!\n")
        chosen_column = int(input("Please enter colum number: "))
        # Fill the global board with player one's token
        global_board = drop_token(global_board, chosen_column)
        # End player one's turn
        current_player = 2
    else:
        print("Player's two move!\n")
        chosen_column = int(input("Please enter colum number: "))
        # Fill the global board with player two's token
        global_board = drop_token(global_board, chosen_column)
        # End player two's turn
        current_player = 1

    print_board(global_board)
