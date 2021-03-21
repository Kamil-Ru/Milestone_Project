# Write a function that can print out a board. 
# Set up your board as a list, where each index 1-9 corresponds with a number on a number pad, 
# so you get a 3 by 3 board representation.

def display_board(board):
    board = print("""
    -------------
    | {} | {} | {} |
    -------------
    | {} | {} | {} |
    ------------- 
    | {} | {} | {} |
    -------------""".format(board[7],board[8],board[9],board[4],board[5], board[6], board[1], board[2], board[3]))
    return board
    
test_board = ['#','X','O','X','O','X','O','X','O','X']
display_board(test_board)