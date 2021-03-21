# Write a function that returns a boolean indicating whether a space on the board is freely available.

def space_check(board, position):
    if board[position] == ' ':
        return True
    else:
        return False

# TEST
# test_board = ['#','X','O','X','O','X','O','X','O','X']
# test_board_2 = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
# print(space_check(test_board, 1))
# print(space_check(test_board_2, 1))
# print(space_check(test_board_2, 5))