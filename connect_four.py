

def print_board(board):
    # x = 1
    for row in board:
        for element in row:
            print(element, end=" ")          # finish end loop
        print()         # print sec row


# have an empty board n stashes
# the board menu, empty dashes
# list comprehension or nested while loops

def initialize_board(num_rows, num_cols):
    return [["-" for _ in range(num_rows)]for _ in range(num_cols)]


# col in the index
def insert_chip(board, col, chip_type):
    row = -1
    for i in range(len(board) - 1, -1, -1):
        if board[i][col] == '-':
            board[i][col] = chip_type
            row = i
            break
    return row


# row: row index returned from insert_chip
    # row is 0
# col: col index entered by the user in the main logic
    # col is 4
def check_if_winner(board, col, row, chip_type):
    # check all rows
    # checks each column
    yeur = 0
    for i in range(len(board[0])):
        if board[row][i] == chip_type:
            yeur += 1
            if yeur == 4:
                return True
        else:
            yeur = 0

    yeur = 0
    for i in range(len(board)):
        if board[i][col] == chip_type:
            yeur += 1
            if yeur == 4:
                return True
        else:
            yeur = 0

    yeur = 0
    i, j = row, col
    while i > 0 and j > 0:
        i -= 1
        j -= 1
    while i < len(board) and j < len(board[0]):
        if board[i][j] == chip_type:
            yeur += 1
            if yeur == 4:
                return True
        else:
            yeur = 0
        i += 1
        j += 1

    yeur = 0
    i, j = row, col
    while i < len(board) - 1 and j > 0:
        i += 1
        j -= 1
    while i >= 0 and j < len(board[0]):
        if board[i][j] == chip_type:
            yeur += 1
            if yeur == 4:
                return True
        else:
            yeur = 0
        i -= 1
        j += 1
    # return False


if __name__ == "__main__":
    num_cols = int(input("What would you like the height of the board to be? "))
    num_rows = int(input("What would you like the length of the board to be? "))
    board = initialize_board(num_rows, num_cols)
    print_board(board)

    print()
    print("Player 1: x\nPlayer 2: o")
    print()
    player = ['x', 'o']
    turn = 0

    while True:
        # player = 1, 2
        curr_play3r = player[turn]
        col = int(input(f"Player {turn + 1}: Which column would you like to choose? "))
        row = insert_chip(board, col, curr_play3r)
        print_board(board)
        if check_if_winner(board, col, row, curr_play3r):
            print(f"Player {turn + 1} won the game!")
            break
        if all('-' not in row for row in board):
            print("Draw. Nobody wins.")
            break
        turn = (turn + 1) % 2


