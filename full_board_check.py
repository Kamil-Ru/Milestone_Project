# Write a function that checks if the board is full and returns a boolean value. 
# True if full, 
# False otherwise.

# OLD
def full_board_check(board):
    for x in board:
        if x == ' ':
            return False
    else:
        return True

# NEW
def full_board_check_2(board):
    return ' ' not in board

#  TEST
test_board = ['O','X','O','X','O','X','O','X','O','X']
print(full_board_check(test_board))

test_board = ['O','X','O','X','O','X','O','X','O','X']
print(full_board_check_2(test_board))