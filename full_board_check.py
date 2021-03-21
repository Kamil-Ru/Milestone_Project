# Write a function that checks if the board is full and returns a boolean value. 
# True if full, 
# False otherwise.

def full_board_check(board):
    for x in board:
        if x == ' ':
            return False
    else:
        return True

#  TEST
test_board = ['O','X','O','X','O','X','O','X','O','X']
print(full_board_check(test_board))